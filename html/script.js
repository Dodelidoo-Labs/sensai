$(document).ready(function() {
    $('#contactForm').submit(function(e) {
        e.preventDefault();

        var name = $('#name').val();
        var email = $('#email').val();
        var message = $('#message').val