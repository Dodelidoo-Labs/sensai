<!DOCTYPE html>
<html>
<head>
    <title>Contact Page</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="contact.js"></script>
</head>
<body>
    <?php include 'header.php'; ?>

    <h1>Contact Us</h1>

    <form id="contact-form" method="post" action="submit.php">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Submit</button>
    </form>

    <?php include 'footer.php'; ?>
</body>
</html>