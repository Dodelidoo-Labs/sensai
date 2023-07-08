HTML:
```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
  <header class="red-header">
    <h1 class="centered-text">Hello World</h1>
  </header>
  <footer class="black-footer">
    <p class="centered-text">Footer Content</p>
  </footer>
</body>
</html>
```

CSS (styles.css):
```css
body {
  margin: 0;
  padding: 0;
}

.red-header {
  background-color: red;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.black-footer {
  background-color: black;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.centered-text {
  color: white;
  text-align: center;
}
```

PHP:
```php
<?php
// No PHP code is required for this task
```