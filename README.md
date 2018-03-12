# Technical Test

The goal of this test is to evaluate your ability:

- index a documentation and do a small frontend search on top of it
- to write content targeted at developers

For this test you will need to create a free Algolia account.
If you need extended quota, reach out to us.

The test is comprised of three parts:

## 1. Indexing

### Instructions

In the docs/ folder you have a copy of our [middleman](https://middlemanapp.com/basics/install/)
based [DocSearch website](https://community.algolia.com/docsearch/).
Part of the exercise is to manage to install the environment using the middleman documentation. 

The goal of this exercise to create an algolia index of all documentation pages of this website via a ruby script.
Each page must be split in several records using the method explained
in the [following blog post](https://blog.algolia.com/how-to-build-a-helpful-search-for-technical-documentation-the-laravel-example/).
To do the split you will need to use an html parser library.

There is a skeleton "algolia indexing command" (docs/extensions/indexer_command.rb) that needs to be completed in order
to create the index.

The skeleton takes care of the interfacing with middleman and is already looping through doc pages only.
This middleman command can be run via the following bash command `bundle exec middleman algolia` from the docs directory. 
 

### Evaluation criteria

- quality of the code
- relevance of the search

### Deliverable

- the updated indexer_command.rb file

## 2. Search frontend

### Instructions

Using [instantsearch.js](https://community.algolia.com/instantsearch.js/v2/),
implement a frontend search based on the index created in step 1.

Since we split the records we now have several records for each page.
Only 1 result should be displayed for a given page (best record of the page should be displayed).  

### Evaluation criteria

- Ability to use instansearch.js on split data
- The right [search parameters](https://www.algolia.com/doc/api-reference/search-api-parameters/) are being used
- Design will not be taken into account in the evaluation.  
  We are expecting a very basic display of the information nothing more.
- No links are needed.

### Deliverable

- a html page. An extra css file and a extra js file are allowed but not mandatory  

## 3. Write a tutorial about step 1.

### Instructions

Based on what you did in the step 1., write a tutorial explaining the process of splitting
html pages using ruby.

### Evaluation criteria

- Quality of rewritten content:
    - accuracy
    - intuitiveness
    - structure
- Voice and tone

### Deliverable

- a markdown file containing the tutorial