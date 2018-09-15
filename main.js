const search = instantsearch({
    appId: 'P1CNOY80LV',
    apiKey: '12a0e2f2e0c7c22ef8220bb905900d10',
    indexName: 'doc-test',
    routing: true
});

  // initialize RefinementList
  search.addWidget(
    instantsearch.widgets.refinementList({
      container: '#refinement-list',
      attributeName: 'categories'
    })
  );

  // initialize SearchBox
  search.addWidget(
    instantsearch.widgets.searchBox({
      container: '#search-box',
      placeholder: 'Search the docs'
    })
  );

  search.addWidget(
    instantsearch.widgets.hits({
      container: '#hits',
      templates: {
        empty: 'No results',
        item: '<em>Hit {{importance}}</em>: {{{_highlightResult.content.value}}}'
      }
    })
  );

// initialize currentRefinedValues
search.addWidget(
instantsearch.widgets.currentRefinedValues({
  container: '#current-refined-values',
  // This widget can also contain a clear all link to remove all filters,
  // we disable it in this example since we use `clearAll` widget on its own.
  clearAll: false
})
);

// initialize clearAll
search.addWidget(
instantsearch.widgets.clearAll({
  container: '#clear-all',
  templates: {
    link: 'Reset everything'
  },
  autoHideContainer: false
})
);

// initialize pagination
search.addWidget(
instantsearch.widgets.pagination({
  container: '#pagination',
  maxPages: 20,
  // default is to scroll to 'body', here we disable this behavior
  scrollTo: false
})
);

search.start();