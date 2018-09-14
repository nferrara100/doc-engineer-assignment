# from algoliasearch import algoliasearch
# from config import Config
from html.parser import HTMLParser
import os


# client = algoliasearch.Client(Config.algolia_key, Config.algolia_secret)
# # index = client.init_index('doc-test-demo')


class DocParser(HTMLParser):
    current_tag = []
    wanted_tags = ['h1', 'h2', 'h3', 'h4', 'p']

    def handle_starttag(self, tag, attrs):
        if tag in self.wanted_tags:
            self.current_tag.append([tag.lower(), ''])

    def handle_endtag(self, tag):
        if tag in self.wanted_tags:
            try:
                if tag == self.current_tag[-1:][0]:
                    print(tag + " : " + self.current_tag[-1:][1])
                self.current_tag.pop()
            except IndexError:
                # pass
                raise IndexError('There is an unknown endtag in the HTML. Remove it and try again.')

    def handle_data(self, data):
        try:
            self.current_tag[-1:][1] += data
        except IndexError:
            pass
            # print("The following text is not nested in the HTML and was not indexed: " + data)


parser = DocParser()
folder = "source"
for file in os.walk(folder, followlinks=True):
    for i in range(len(file[2])):
        filename = file[0] + os.sep + file[2][i]
        if filename[-5:] == ".html":
            with open(filename, 'r') as webpage:
                parser.feed(webpage.read())
print("Done")
