// AJAX form submission code
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Get form data
    var formData = new FormData(this);
    
    // Send AJAX request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'submit.php', true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Handle successful form submission
        } else {
            // Handle form submission error
        }
    };
    xhr.send(formData);
});