# Technical Test

The goal of this test is to evaluate your ability to:

1. Create an Algolia search index from HTML pages
2. Provide a front-end search on top of it
3. Write a tutorial on how to create the Algolia index

For this test, you will need to create a [free Algolia account](https://www.algolia.com/users/sign_up).
If you need an extended quota, reach out to me at maxime.locqueville@algolia.com.

The test is comprised of 3 parts:

## 1. Indexing

### Instructions

In the `source/` folder you have 4 HTML files. 

The goal of this exercise to create an Algolia index for all 4 pages.
Each page must be split into several records using the method explained
in the [following blog post](https://blog.algolia.com/how-to-build-a-helpful-search-for-technical-documentation-the-laravel-example/).
To do the split, you will need to use an HTML parser library.

You can use any of the following programing languages: PHP, Ruby, JavaScript or Python.

Here are the docs to their respective Algolia API clientc:
[PHP](https://www.algolia.com/doc/api-client/php/getting-started/), [Ruby](https://www.algolia.com/doc/api-client/ruby/getting-started/), [JavaScript](https://www.algolia.com/doc/api-client/javascript/getting-started/), [Python](https://www.algolia.com/doc/api-client/python/getting-started/).

### Evaluation criteria

- Quality of the code (readable, optimized, well-formatted)
- Relevance of the search (you can check it directly in your Algolia dashboard by doing searches)

### Deliverable

- A file that contains the source code of the indexing. 

## 2. Search front-end

### Instructions

Using [InstantSearch.js](https://community.algolia.com/instantsearch.js/v2/),
implement a front-end search based on the index created in step 1.

Since we split the records we now have several records for each page.
Only 1 result should be displayed for a given page (best record of the page should be displayed).  

### Evaluation criteria

- Ability to use InstantSearch.js on split data
- The right [search parameters](https://www.algolia.com/doc/api-reference/search-api-parameters/) are being used
- Design will not be taken into account in the evaluation.  
  We are expecting a very basic display of the information, nothing more.

### Deliverable

- An HTML page. Extra CSS and JS files are allowed but not mandatory. You also don't have to add a build step or transpile anything if you use ES6+.

## 3. Write a tutorial about step 1.

### Instructions

Based on what you did in step 1, write a tutorial explaining the process of splitting
HTML pages (with the language that you chose).

### Evaluation criteria

- Quality of written content:
    - accuracy
    - intuitiveness
    - structure
- Voice and tone

### Deliverable

- A Markdown file containing the tutorial

---

As for the full deliverable of this assignment, you can share a GitHub project with us, or send us
a zip file with everything in it. Take into account that the easier it is for us to run things, the better. Please provide good developer experience.

Good Luck 🍀 Have Fun 🎉
