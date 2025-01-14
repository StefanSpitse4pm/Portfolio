<?php
session_start();
$hardcodedtoken = '9832576';
if ($_SERVER['REQUEST_METHOD'] == "POST") {
    $token = $_POST['token'];
    if ($token == $hardcodedtoken){ 
        $_SESSION['token'] = 'loggedin';
    } 
    else {  
        echo '<script type="text/javascript">';
        echo 'alert("Warning:token is niet correct");';
        echo '</script>';
    }
}

if ($_SERVER['REQUEST_METHOD'] == 'GET' && !empty($_GET['nologgin'])){
    echo '<script type="text/javascript">';
    echo 'alert("Warning: Je hebt een token nodig om die pagina te kunnen zien");';
    echo '</script>';
}

?>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stefan Spitse</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <main>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="Portfolio.php">Portfolio</a></li>
                <li><a href="aboutme.html">About me</a></li>
                <li><a href="https://www.linkedin.com/in/stefan-spitse/">Contact me</a></li>
            </ul>
        </nav>
        <div class="main">
            <div class="container">
                <a href="Portfolio.php">
                    <h1>Stefan Spitse</h1>
                    <h2>Klik hier voor mijn Portfolio!</h2> 
                </a>    
            </div>
            <?php if (empty($_SESSION['token'])) {
            ?>
           <div class="tokeninput">
                <h2>Put your token here</h2>
                <form action="index.php" method="POST">
                    <label for="token">Token </label>
                    <input type="text" name="token" id="token">
                    <input type="submit" value="Login">
                </form>
           </div>
           <php ;<?php }?> 
        </div>
    </main>
</body>
</html>