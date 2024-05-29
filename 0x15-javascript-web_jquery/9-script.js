let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function(data) {
    $('#hello').text(data.hello);
}).fail(function(xhr, status, error) {
    console.error('Error fetching translation:', error);
});
