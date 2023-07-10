$(document).ready(function() {
    $('#contact-form').submit(function(e) {
        e.preventDefault();

        var form = $(this);
        var url = form.attr('action');
        var method = form.attr('method');
        var data = form.serialize();

        $.ajax({
            url: url,
            type: method,
            data: data,
            dataType: 'json',
            success: function(response) {
                if (response.success) {
                    alert(response.message);
                    form[0].reset();
                } else {
                    alert(response.message);
                }
            },
            error: function() {
                alert('An error occurred while submitting the form');
            }
        });
    });
});