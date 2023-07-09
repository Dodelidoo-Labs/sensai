$(document).ready(function() {
    $('#contact-form').submit(function(e) {
        e.preventDefault();

        var name = $('#name').val();
        var email = $('#email').val();
        var message = $('#message').val();

        $.ajax({
            url: 'submit.php',
            type: 'POST',
            data: {
                name: name,
                email: email,
                message: message
            },
            success: function(response) {
                $('#response').html(response);
                $('#contact-form')[0].reset();
            }
        });
    });
});