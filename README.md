# Technical Test

The goal of this test is to evaluate your ability to:

1. Create an Algolia search index from a documentation website
2. Provide a frontend search on top of it
3. Write a tutorial on how to create such Algolia index

For this test you will need to create a [free Algolia account](https://www.algolia.com/users/sign_up).
If you need an extended quota, reach out to me at maxime.locqueville@algolia.com.

The test is comprised of three parts:

## 1. Indexing

### Instructions

In the docs/ folder you have a copy of our [middleman](https://middlemanapp.com/basics/install/)
based [DocSearch website](https://community.algolia.com/docsearch/).

There's a [skeleton command](./docs/extensions/indexer_command.rb) (in `doc-engineer-assignment/docs/extensions/indexer_command.rb`) that takes care of the interfacing with middleman and is already looping through doc pages only.
This middleman command can be run via the following bash command `bundle exec middleman algolia` from the docs directory.

**Your goal**: complete this command to make it index the documentation content into Algolia.
Each page must be split in several records using the method explained in the
[following blog post](https://blog.algolia.com/how-to-build-a-helpful-search-for-technical-documentation-the-laravel-example/).
To do the split you will need to use an html parser library.

### Evaluation criteria

- Quality of the code
- Relevance of the search (that you can check in your Algolia dashboard by doing searches)

### Deliverable

- The updated indexer_command.rb file

## 2. Search frontend

### Instructions

Using [InstantSearch.js](https://community.algolia.com/instantsearch.js/v2/),
implement a frontend search based on the index created in step 1.

Since we split the records we now have several records for each page.
Only 1 result should be displayed for a given page (best record of the page should be displayed).  

### Evaluation criteria

- Ability to use InstantSearch.js on split data
- The right [search parameters](https://www.algolia.com/doc/api-reference/search-api-parameters/) are being used
- Design will not be taken into account in the evaluation.  
  We are expecting a very basic display of the information nothing more.
- No links handling is needed.
- Ease of running of the demo.

### Deliverable

- An html page.

## 3. Write a tutorial about step 1.

### Instructions

Based on what you did in the step 1., write a tutorial explaining the process of splitting
html pages using ruby.

### Evaluation criteria

- Quality of written content:
    - accuracy
    - intuitiveness
    - structure
- Voice and tone

### Deliverable

- A markdown file containing the tutorial

---

As for the full deliverable of this assignment, you can share a GitHub project with us, or send us
a zipfile with everything inside it. Take into account that the easiest for us to run things, the better,
provide a good developer experience.

Good Luck 🍀 Have Fun 🎉
