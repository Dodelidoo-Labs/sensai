$(document).ready(function() {
    $('#contactForm').submit(function(e) {
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
            }
        });
    });
});
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Process the form data (e.g. send email, save to database, etc.)

    // Return a response message
    echo "Thank you for your message, $name!";
}
?>