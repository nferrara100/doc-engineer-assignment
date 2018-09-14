from algoliasearch import algoliasearch
from config import Config
from html.parser import HTMLParser
import os


class DocParser(HTMLParser):
    current_tag = ''
    current_text = ''
    wanted_tags = ['h1', 'h2', 'h3', 'h4']

    def __init__(self):
        self.client = algoliasearch.Client(Config.algolia_key, Config.algolia_secret)
        self.index = self.client.init_index('doc-test')
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag in self.wanted_tags:
            if self.current_text != "":
                res = self.index.add_object({"tag": "p", "super": self.current_tag, "text": self.current_text})
            self.current_tag = tag.lower()

    def handle_endtag(self, tag):
        if tag in self.wanted_tags:
            res = self.index.add_object({"tag": tag, "text": self.current_text})
            self.current_text = ''

    def handle_data(self, data):
        self.current_text += data


parser = DocParser()
folder = "source"
for file in os.walk(folder, followlinks=True):
    for i in range(len(file[2])):
        filename = file[0] + os.sep + file[2][i]
        if filename[-5:] == ".html":
            with open(filename, 'r') as webpage:
                parser.feed(webpage.read())
