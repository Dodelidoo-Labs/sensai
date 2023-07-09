<?php
// Handle form submission
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// Process form data and send email, save to database, etc.

// Return response
$response = array('success' => true);
header('Content-Type: application/json');
echojson_encode($response);