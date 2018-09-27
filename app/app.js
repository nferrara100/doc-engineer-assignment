// Format each result from a search
function formatHit(hit) {
    const tags = ['h1', 'h2', 'h3', 'h4', 'content'];
    var formatted = '<a href="' + hit.link + '#' + hit.hash + '">';
    var linked = false;
    for(let i = 0; i < 4; i++){
        // Do this for each of the heading tags
        if (hit[tags[i]]) {
            formatted += hit._highlightResult[tags[i]].value;
            // Close the <a> tag after the first hit
            if (!linked) {
                formatted += '</a><br /> ';
                linked = true;
            }
            else {
                formatted += ": "
            }
        }
    }
    // Add all of the content of the page
    if (hit.content) {
        formatted += hit._snippetResult.content.value
    }
    return formatted + '<br /><br />';
}

// Set up the Instant Search API
const search = instantsearch({
	appId: 'P1CNOY80LV',
	apiKey: '12a0e2f2e0c7c22ef8220bb905900d10',
	indexName: 'doc-ex',
    urlSync: true
});

// initialize SearchBox
search.addWidget(
	instantsearch.widgets.searchBox({
		container: '#search-input',
		placeholder: 'Search the docs'
	})
);

// Displays the result of the search
search.addWidget(
	instantsearch.widgets.hits({
		container: '#hits',
		templates: {
			empty: "We didn't find any results for the search <em>\"{{query}}\"</em>",
			item: hit => formatHit(hit)
		}
	})
);

search.start();
