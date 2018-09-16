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
    headings = ['', '', '', '']
    unwanted_tags = ['audio', 'canvas', 'map', 'meta', 'object', 'script', 'source', 'style', 'video']

    def __init__(self, algolia, page):
        self.algolia = algolia
        self.page = page.replace(os.sep, '/')
        self.link = self.page
        self.position = False
        self.unwanted = False
        self.importance = -1
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        # print(tag + " " + repr(attrs))
        if tag in self.wanted_tags:
            self.save_record(self.current_text.strip())
            self.position = False
            self.unwanted = False
            self.current_tag = tag
            self.link = self.page
            self.importance = self.wanted_tags.index(self.current_tag)
        elif tag == 'a' and self.position is False:
            for name, value in attrs:
                if name == 'id':
                    self.link += '#' + value
                    self.position = True
        elif tag in self.unwanted_tags:
            self.unwanted = True

    def handle_endtag(self, tag):
        if tag in self.wanted_tags:
            self.unwanted = False
            self.headings[self.wanted_tags.index(self.current_tag)] = self.current_text.strip()
            self.save_record()

    def handle_data(self, data):
        if self.unwanted is False:
            self.current_text += data

    def save_record(self, content=''):
        if self.current_text.strip() != "":
            obj = {"link": self.link, "importance": self.importance}
            for i in range(self.importance + 1):
                obj[self.wanted_tags[i]] = self.headings[i]
            if content != '':
                obj['content'] = content
            res = self.algolia.index.add_object(obj)
            self.current_text = ''


def index_files():
    folder = "source"
    algolia = Algolia()
    for file in os.walk(folder, followlinks=True):
        for i in range(len(file[2])):
            filename = file[0] + os.sep + file[2][i]
            if filename[-5:] == ".html":
                with open(filename, 'r') as webpage:
                    parser = DocParser(algolia, filename)
                    parser.feed(webpage.read())


if __name__ == "__main__":
    index_files()
