<?php
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// Process the form data here

// Send email
$to = 'contact@example.com';
$subject = 'New Contact Form Submission';
$body = "Name: $name\nEmail: $email\nMessage: $message";
$headers = "From: $email";

if (mail($to, $subject, $body, $headers)) {
  echo 'success';
} else {
  echo 'error';
}
?>
