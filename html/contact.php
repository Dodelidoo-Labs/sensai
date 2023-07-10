<?php
include 'header.php';
?>

<h1>Contact Us</h1>

<form id="contact-form">
  <input type="text" name="name" placeholder="Your Name">
  <input type="email" name="email" placeholder="Your Email">
  <textarea name="message" placeholder="Your Message"></textarea>
  <button type="submit">Submit</button>
</form>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
  $(document).ready(function() {
    $('#contact-form').submit(function(e) {
      e.preventDefault();
      var formData = $(this).serialize();
      $.ajax({
        url: 'submit.php',
        type: 'POST',
        data: formData,
        success: function(response) {
          alert('Message sent successfully!');
        }
      });
    });
  });
</script>

<?php
include 'footer.php';
?>
