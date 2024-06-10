
export const events = (dataTable) => {
    // on change pages

    let searchQuery = new URLSearchParams(window.location.search).get('search')

    if (searchQuery === null)
        searchQuery = ''

    dataTable.on('datatable.perpage', function(perPage) {
        window.location.search = '?page=1&entries=' + perPage +
        "&search=" + searchQuery ;

        console.log(perPage)
    });
}