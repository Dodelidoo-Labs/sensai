<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // Process the form data (e.g. send email, save to database, etc.)

    // Return a response
    echo 'success';
}
?>
