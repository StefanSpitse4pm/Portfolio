<?php 

if (empty($_SESSION['token'])) {
    header('Location: index.html');
} 

?>


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stefan Spitse</title>
    <link rel="stylesheet" href="../css//style.css">
    <script src="../js/portfolio.js"></script>
</head>
<body>
    
    <div id="popup">
        <h2>Token hier</h3>
        <form action="Portfolio.html">
            <input type="text" required>
            <button type="submit">Lets a go</button>
        </form>
    </div>
   <main id="content">
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="Portfolio.html">Portfolio</a></li>
                <li><a href="aboutme.html">About me</a></li>
                <li><a href="https://www.linkedin.com/in/stefan-spitse/">Contact me</a></li>
            </ul>
        </nav>
        
        <div class="main"> 
            <a href="../files/reflectie verslag.pdf" target="_blank">
                <div class="file">
                    <p>reflectie Verslag</p>
                </div>
            </a>
            <a href="../files/Feedback van periode 1.pdf" target="_blank">
                <div class="file">
                    <p>feed back periode 1</p>
                </div>
            </a>
            <a href="../files/Belbin feedback periode 1.pdf" target="_blank">
                <div class="file">
                    <p>belbin feedback periode 1</p>
                </div>
            </a>
            <a href="" target="_blank">
                <div class="file">
                    <p>Feedback periode 2</p>
                </div>
            </a>
            <a href="../files/Plan van aanpak.pdf" target="_blank">
                <div class="file">
                    <p>Plan van aanpak</p>
                </div>
            </a>
            <a href="../files/presentatie voorbereiding.pdf" target="_blank">
                <div class="file">
                    <p>Groeps presentatie voorbereiding</p>
                </div>
            </a>
            <a href="../files/GroepspresentatieINF1B.pdf" target="_blank">
                <div class="file">
                    <p>Positief feedback groeps presentatie</p>
                </div>
            </a>
            <a href="../files/agenda.pdf" target="_blank">
                <div class="file">
                    <p>Agenda vegadering</p>
                </div>
            </a>
            <a href="../files/Notulen_plenair_17_december_2024.pdf" target="_blank">
                <div class="file">
                    <p>Notulen</p>
                </div>
            </a><a href="../files/Portfolio 2022_2023(2).pdf" target="_blank">
                <div class="file">
                    <p>Edumundo opdrachten</p>
                </div>
            </a>
            <a href="../files/">
                <div class="file">
                    <p></p>
                </div>
            </a>
        </div>

        <script>
            function getCookie(name) {
            const cookies = document.cookie.split(';').map(cookie => cookie.trim());
            for (const cookie of cookies) {
                if (cookie.startsWith(name + '=')) {
                return cookie.split('=')[1];
                }
            }
            return null;
            }

            const existingCookie = getCookie("session_id")
            const popup = document.getElementById("popup")
            const content = document.getElementById("content")
            
            // if (!existingCookie) {
            //     popup.style.display = "grid";
            //     content.classList.add('dimmed')
            // }
        </script>
    </main>    
</body>
</html>