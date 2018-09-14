from algoliasearch import algoliasearch
from config import Config
from html.parser import HTMLParser
import os


class Algolia:
    def __init__(self):
        self.client = algoliasearch.Client(Config.algolia_key, Config.algolia_secret)
        self.index = self.client.init_index('doc-test')


class DocParser(HTMLParser):
    current_tag = ''
    current_text = ''
    wanted_tags = ['h1', 'h2', 'h3', 'h4']
    unwanted_tags = ['canvas', 'data', 'datalist', 'map', 'meta', 'object', 'param', 'script', 'source', 'style',
                     'video']

    def __init__(self, algolia, page):
        self.algolia = algolia
        self.page = page.replace(os.sep, '/')
        self.position = 0
        self.unwanted = False
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag in self.wanted_tags:
            if self.current_text.strip() != "":
                res = self.algolia.index.add_object({"page": self.page, "line": self.position, "tag": "p",
                                                     "super": self.current_tag, "text": self.current_text.strip()})
            self.unwanted = False
            self.position = self.getpos()[0]
            self.current_tag = tag.lower()
        elif tag in self.unwanted_tags:
            self.unwanted = True

    def handle_endtag(self, tag):
        if tag in self.wanted_tags:
            self.unwanted = False
            if self.current_text.strip() != "":
                res = self.algolia.index.add_object({"page": self.page, "line": self.position, "tag": tag,
                                                 "text": self.current_text.strip()})
            self.current_text = ''

    def handle_data(self, data):
        if self.unwanted is False:
            self.current_text += data


folder = "source"
algolia = Algolia()
for file in os.walk(folder, followlinks=True):
    for i in range(len(file[2])):
        filename = file[0] + os.sep + file[2][i]
        if filename[-5:] == ".html":
            with open(filename, 'r') as webpage:
                parser = DocParser(algolia, filename)
                parser.feed(webpage.read())
