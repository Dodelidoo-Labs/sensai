<!DOCTYPE html>
<html>
<head>
    <title>Contact</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="script.js"></script>
</head>
<body>
    <?php include 'header.php'; ?>

    <h1>Contact</h1>
    <form id="contactForm" method="post">
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
        </div>
        <div>
            <input type="submit" value="Submit">
        </div>
    </form>

    <?php include 'footer.php'; ?>
</body>
</html>