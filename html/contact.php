<!DOCTYPE html>
<html>
<head>
    <title>Contact Page</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script>
        $(document).ready(function() {
            $('#contactForm').submit(function(e) {
                e.preventDefault();
                
                var formData = $(this).serialize();
                
                $.ajax({
                    type: 'POST',
                    url: 'submit.php',
                    data: formData,
                    success: function(response) {
                        alert(response);
                    }
                });
            });
        });
    </script>
</head>
<body>
    <?php include 'header.php'; ?>
    
    <h1>Contact Page</h1>
    
    <form id="contactForm" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required><br><br>
        
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required><br><br>
        
        <label for="message">Message:</label>
        <textarea name="message" id="message" required></textarea><br><br>
        
        <input type="submit" value="Submit">
    </form>
    
    <?php include 'footer.php'; ?>
</body>
</html>