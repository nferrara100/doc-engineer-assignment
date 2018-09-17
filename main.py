from algoliasearch import algoliasearch
from config import Config
from html.parser import HTMLParser
import os
import time


class Algolia:
    def __init__(self):
        self.client = algoliasearch.Client(Config.algolia_key, Config.algolia_secret)
        self.index = self.client.init_index('doc-test')


class DocParser(HTMLParser):

    def __init__(self, algolia, page):
        self.algolia = algolia
        self.page = page.replace(os.sep, '/')
        self.hash = ''
        self.position = False
        self.unwanted = False
        self.importance = -1
        self.headings = ['', '', '', '']
        self.current_tag = ''
        self.current_text = ''
        self.wanted_tags = ['h1', 'h2', 'h3', 'h4']
        self.unwanted_tags = ['audio', 'canvas', 'map', 'meta', 'object', 'script', 'source', 'style', 'video']
        self.total_records = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        # print(tag + " " + repr(attrs))
        if tag in self.wanted_tags:
            self.save_record(self.current_text.strip())
            self.position = False
            self.unwanted = False
            self.current_tag = tag
            self.hash = ''
            self.importance = self.wanted_tags.index(self.current_tag)
        elif tag == 'a' and self.position is False:
            for name, value in attrs:
                if name == 'id':
                    self.hash = value
                    self.position = True
        elif tag in self.unwanted_tags:
            self.unwanted = True

    def handle_endtag(self, tag):
        if tag in self.wanted_tags:
            self.unwanted = False
            self.headings[self.importance] = self.current_text.strip()
            self.save_record()

    def handle_data(self, data):
        if self.unwanted is False:
            self.current_text += data

    def save_record(self, content=''):
        if self.current_text.strip() != "":
            record = {}
            for i in range(self.importance + 1):
                if self.headings[i] != '':
                    record[self.wanted_tags[i]] = self.headings[i]
            if content != '':
                record['content'] = content
            record['link'] = self.page
            record['hash'] = self.hash
            record['importance'] = self.importance
            res = self.algolia.index.add_object(record)
            if res['objectID']:
                self.total_records += 1
            else:
                print("Error adding " + self.current_tag + " to Algolia's database")
            self.current_text = ''


def index_files():
    folder = "source"
    algolia = Algolia()
    total_records = 0
    start_time = time.time()
    for file in os.walk(folder, followlinks=True):
        for i in range(len(file[2])):
            filename = file[0] + os.sep + file[2][i]
            if filename[-5:] == ".html":
                with open(filename, 'r', encoding='utf-8') as webpage:
                    parser = DocParser(algolia, filename)
                    parser.feed(webpage.read())
                    total_records += parser.total_records

    add_result = algolia.index.set_settings({
        'attributeForDistinct': 'link',
        'distinct': 1,
        'attributesToSnippet': [
            'content:20'
        ],
        'snippetEllipsisText': '…'
    })
    if not isinstance(add_result['taskID'], int):
        print("Error creating new Algolia settings")

    print("Added {:0d} records in {:0.4f} seconds.".format(total_records, (time.time() - start_time) / 1000))


if __name__ == "__main__":
    index_files()
