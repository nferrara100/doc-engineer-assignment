from algoliasearch import algoliasearch
from config import Config
from html.parser import HTMLParser
import os
import time


# Save Algolia settings in its own reusable class
class Algolia:
    def __init__(self):
        self.client = algoliasearch.Client(Config.algolia_key, Config.algolia_secret)
        self.index = self.client.init_index('doc-ex')


# Take given HTML text and parse into searchable Algolia database
class DocParser(HTMLParser):

    # Needs an Algolia class and the page in a string format to proceed.
    def __init__(self, algolia, page):
        self.algolia = algolia
        # The replace call ensures compatibility with Windows
        self.page = page.replace(os.sep, '/')
        self.location = ''
        self.unwanted = False
        self.importance = -1
        self.headings = ['', '', '', '']
        self.current_tag = ''
        self.current_text = ''
        self.wanted_tags = ['h1', 'h2', 'h3', 'h4']
        # The inner contents of these tags should not be displayed and are thus not recorded
        self.unwanted_tags = ['audio', 'canvas', 'map', 'meta', 'object', 'script', 'source', 'style', 'video']
        self.total_records = 0
        HTMLParser.__init__(self)

    # Every time a start tag is encountered in the document save it in case it contains something useful
    def handle_starttag(self, tag, attrs):
        # See if this tag should be recorded separately
        if tag in self.wanted_tags:
            self.save_record(self.current_text.strip())
            self.unwanted = False
            self.current_tag = tag
            self.location = ''
            # The lower the importance number the more important it is
            self.importance = self.wanted_tags.index(self.current_tag)
        # If a location isn't saved use this link as a hash bookmark
        elif tag == 'a' and self.location == '':
            for name, value in attrs:
                if name == 'id':
                    self.location = value
        # This prevents data from being recorded that is not meant to be human readable
        elif tag in self.unwanted_tags:
            self.unwanted = True

    # Once an element is completed save it if it was useful. Let it become part of the next record if it was not.
    def handle_endtag(self, tag):
        if tag in self.wanted_tags:
            self.unwanted = False
            self.headings[self.importance] = self.current_text.strip()
            self.save_record()

    # For everything inside a tag if it is one of the wanted tags save that data to current_text
    def handle_data(self, data):
        if self.unwanted is False:
            self.current_text += data

    # Save the collected data so far in the class to Algolia and then wipe that data locally so it is not added again
    def save_record(self, content=''):
        if self.current_text.strip() != "":
            record = {}
            # Save each of the heading tags in their own field
            for i in range(self.importance + 1):
                if self.headings[i] != '':
                    record[self.wanted_tags[i]] = self.headings[i]
            if content != '':
                record['content'] = content
            record['page'] = self.page
            record['location'] = self.location
            record['importance'] = self.importance
            res = self.algolia.index.add_object(record)
            if res['objectID']:
                self.total_records += 1
            else:
                print("Error adding " + self.current_tag + " to Algolia's database")
            self.current_text = ''


# Main entry point. Index files and send to Algolia's server for future searches.
def index_files():
    folder = "source"  # Change this if the file structure changes
    algolia = Algolia()

    # For final output statistics
    total_records = 0
    start_time = time.time()

    # Crawl all files in the given folder
    for file in os.walk(folder, followlinks=True):
        for i in range(len(file[2])):
            filename = file[0] + os.sep + file[2][i]

            # Only parse HTML files
            if filename[-5:] == ".html":
                # Open the file and use the DocParser class to turn the HTML into usable data
                with open(filename, 'r', encoding='utf-8') as webpage:
                    parser = DocParser(algolia, filename)
                    parser.feed(webpage.read())
                    total_records += parser.total_records

    # Once parsing is complete set Algolia's settings so that search's are returned properly
    add_result = algolia.index.set_settings({
        'attributeForDistinct': 'page',
        'distinct': 1,
        'attributesToSnippet': [
            'content:20'
        ],
        'snippetEllipsisText': '…'
    })
    # Basic debugging verification that the settings change was successful. This is a guide to users and not a
    # substitute for thorough testing in production environments.
    if not isinstance(add_result['taskID'], int):
        print("Error creating new Algolia settings")

    # Useful statistics to display upon completion.
    print("Added {:0d} records in {:0.4f} seconds.".format(total_records, (time.time() - start_time) / 1000))


# Start the main execution of the script only if it is run directly (i.e. not imported)
if __name__ == "__main__":
    index_files()
