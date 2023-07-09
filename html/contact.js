$(document).ready(function() {
    $('#contact-form').submit(function(e) {
       ```javascript
        e.preventDefault(); // Prevent form submission

        var form = $(this);
        var url = form.attr('action');
        var method = form.attr('method');
        var data = form.serialize();

        $.ajax({
            url: url,
            type: method,
            data: data,
            success: function(response) {
                alert(response); // Display success message
                form.trigger('reset'); // Reset the form
            },
            error: function(xhr, status, error) {
                console.log(xhr.responseText); // Display error message in console
            }
        });
    });
});