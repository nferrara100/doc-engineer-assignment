# Technical Test

The goal of this test is to evaluate your ability to:

1. Create an Algolia search index from a html pages
2. Provide a frontend search on top of it
3. Write a tutorial on how to create such Algolia index

For this test you will need to create a [free Algolia account](https://www.algolia.com/users/sign_up).
If you need an extended quota, reach out to me at maxime.locqueville@algolia.com.

The test is comprised of three parts:

## 1. Indexing

### Instructions

In the source/ folder you have 4 html files. 

The goal of this exercise to create an algolia index for those 4 pages.
Each page must be split in several records using the method explained
in the [following blog post](https://blog.algolia.com/how-to-build-a-helpful-search-for-technical-documentation-the-laravel-example/).
To do the split you will need to use an html parser library.

You can use any of the following programing languages: php, ruby, javascript, python.

Here is the docs to their respective algolia api client:
[php](https://www.algolia.com/doc/api-client/php/getting-started/), [ruby](https://www.algolia.com/doc/api-client/ruby/getting-started/), [javascript](https://www.algolia.com/doc/api-client/javascript/getting-started/), [python](https://www.algolia.com/doc/api-client/python/getting-started/)

### Evaluation criteria

- Quality of the code
- Relevance of the search (that you can check in your Algolia dashboard by doing searches)

### Deliverable

- A file that contains the source code of the indexing. 

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

### Deliverable

- a html page. An extra css file and a extra js file are allowed but not mandatory

## 3. Write a tutorial about step 1.

### Instructions

Based on what you did in the step 1., write a tutorial explaining the process of splitting
html pages (with the language that you choose).

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
