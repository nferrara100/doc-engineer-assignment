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
        self.position = ''
        self.unwanted = False
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag in self.wanted_tags:
            if self.current_text.strip() != "":
                pass
                importance = self.wanted_tags.index(self.current_tag)
                # res = self.algolia.index.add_object({"link": self.page + '#' + self.position,
                #                                      "importance": 4 + importance,
                #                                      "content": self.get_current_text.strip()})
            # Need multiple tags in one result
            self.unwanted = False
            self.current_tag = tag
            self.position = ''
            for attr in attrs:
                if attr[0] == 'id':
                    self.position = attr[1]
        elif tag in self.unwanted_tags:
            self.unwanted = True

    def handle_endtag(self, tag):
        if tag in self.wanted_tags:
            self.unwanted = False
            self.headings[self.wanted_tags.index(self.current_tag)] = self.current_text
            if self.current_text.strip() != "":
                importance = self.wanted_tags.index(self.current_tag)
                obj = {"link": self.page + '#' + self.position, "importance": importance,
                       self.current_tag: self.current_text.strip()}
                for i in range(importance):
                    obj[self.wanted_tags[i]] = self.headings[i]
                res = self.algolia.index.add_object(obj)
            self.current_text = ''

    def handle_data(self, data):
        if self.unwanted is False:
            self.current_text += data


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
