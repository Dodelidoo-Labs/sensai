<?php include 'header.php'; ?>

<main>
    <h2>Contact Page</h2>
    <form id="contact-form" method="post" action="submit.php">
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
</main>

<?php include 'footer.php'; ?>
