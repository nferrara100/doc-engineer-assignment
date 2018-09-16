const search = instantsearch({
    appId: 'P1CNOY80LV',
    apiKey: '12a0e2f2e0c7c22ef8220bb905900d10',
    indexName: 'doc-test',
    routing: true
});

  // initialize SearchBox
  search.addWidget(
    instantsearch.widgets.searchBox({
      container: '#search-box',
      placeholder: 'Search the docs'
    })
  );

  const hitTemplate = '<a href="{{{link}}}">{{{h1}}}' +
      '</a><br/>{{{h2}}}<br/><br/>'


  search.addWidget(
    instantsearch.widgets.hits({
      container: '#hits',
      templates: {
        empty: 'No results',
        item: hitTemplate
      }
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
