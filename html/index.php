<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    #header {
      background-color: red;
      height: 100px;
      width: 100%;
    }

    #footer {
      background-color: black;
      height: 50px;
      width: 100%;
    }

    #content {
      text-align: center;
      font-size: 24px;
    }
  </style>
</head>
<body>
  <div id="header"></div>
  <div id="content">
    <?php
      if (isset($_GET['hello'])) {
        echo $_GET['hello'];
      } else {
        echo "Hello World";
      }
    ?>
  </div>
  <div id="footer"></div>
</body>
</html>