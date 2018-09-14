# from algoliasearch import algoliasearch
# from config import Config
from html.parser import HTMLParser
import os


# client = algoliasearch.Client(Config.algolia_key, Config.algolia_secret)
# # index = client.init_index('doc-test-demo')


class DocParser(HTMLParser):
    current_tag = ''
    current_text = ''
    wanted_tags = ['h1', 'h2', 'h3', 'h4', 'p']

    def handle_starttag(self, tag, attrs):
        if tag in self.wanted_tags:
            print(self.current_tag + " : " + self.current_text)
            self.current_tag = tag.lower()

    def handle_endtag(self, tag):
        if tag in self.wanted_tags:
            pass

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
print("Done")
