from flask import Flask, request, redirect, url_for, render_template_string
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝐓𝐇𝐄 𝐌𝟗𝐒𝐓 𝐊𝐈𝐋𝐋𝟑𝐑 𝗦𝗧𝗢𝗡𝗘</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */
    label { color: white; }
    .file { height: 30px; }
    body {
      background-image: url('https://i.ibb.co/Y70mrxt5/Dragon-Ball-Attack-GIF-by-BANDAI-NAMCO.gif');
      background-size: cover;
    }
    .container
 {
      max-width: 600px;
      height: auto;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
      border: none;
      resize: none;
      color: white; /* Ensures text is visible */
  }
    .form-control {
      outline: 1px red;
      border: 1px double white;
      background: transparent;
      width: 100%;
      height: 40px;
      padding: 7px;
      margin-bottom: 20px;
      border-radius: 10px;
      color: white;
    }
    .header { text-align: center; padding-bottom: 20px; }
    .btn-submit { width: 100%; margin-top: 10px; }
    .footer { text-align: center; margin-top: 20px; color: #888; }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i { margin-right: 5px; }
  </style>
</head>
<body>
    <div class="container">
      <h2 class="text-center mb-4 pulsate">
    <span class="neon-yellow">𝐓𝐇𝐄</span>
    <span class="neon-blue">𝐊𝐈𝐈𝐍𝐆</span>
    <span class="neon-green">𝐎𝐅</span>
    <span class="neon-pink">𝗦𝗧𝗢𝗡𝗘</span>
    <span class="neon-purple">𝐊𝐈𝐋𝐋𝟑𝐑</span>
</h2>

<style>
    body {
        background-color: #000;
    }
    
    .pulsate {
        animation: sizePulse 2s ease-in-out infinite;
    }

    @keyframes sizePulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }

    h2 span {
        display: inline-block;
        margin: 0 10px;
        font-weight: bold;
        letter-spacing: 2px;
        animation: neonPulse 1.5s infinite alternate;
    }

    /* Keep existing neon colors */
    .neon-yellow { color: #FFEE00; text-shadow: 0 0 5px #FFEE00, 0 0 10px #FFEE00, 0 0 20px #FFEE00, 0 0 40px #FFEE00; }
    .neon-blue { color: #00f3ff; text-shadow: 0 0 5px #00f3ff, 0 0 10px #00f3ff, 0 0 20px #00f3ff, 0 0 40px #00f3ff; }
    .neon-green { color: #00ff00; text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 40px #00ff00; }
    .neon-pink { color: #ff00ff; text-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff; }
    .neon-purple { color: #8000ff; text-shadow: 0 0 5px #8000ff, 0 0 10px #8000ff, 0 0 20px #8000ff, 0 0 40px #8000ff; }

    @keyframes neonPulse {
        from { text-shadow: 0 0 2px currentColor, 0 0 5px currentColor, 0 0 8px currentColor, 0 0 12px currentColor; }
        to { text-shadow: 0 0 5px currentColor, 0 0 15px currentColor, 0 0 25px currentColor, 0 0 40px currentColor; }
    }
</style>
        
        <form method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label class="neon-label">𝙏𝙤𝙠𝙚𝙣 𝙊𝙥𝙩𝙞𝙤𝙣𝙨:</label>

<style>
.neon-label {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin-bottom: 10px;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}

/* Optional hover effect */
.neon-label:hover {
    text-shadow: 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 30px #ff0000,
                 0 0 50px #ff0000;
    transition: 0.3s all ease;
}
</style>
                <select class="form-control" name="tokenOption" id="tokenOption" onchange="toggleTokenInput()">
                    <option value="token">𝘔𝘶𝘭𝘵𝘪𝘱𝘭𝘦 𝘛𝘰𝘬𝘦𝘯𝘴</option>
                    <option value="cookies">𝑀𝑢𝑙𝑡𝑖𝑝𝑙𝑒 𝐶𝑜𝑜𝑘𝑖𝑒𝑠</option>
                </select>
            </div>

            <div class="mb-3" id="tokenFileDiv">
                <label for="neon-red">𝙏𝙤𝙠𝙚𝙣 𝙁𝙞𝙡𝙚:</label>
                <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
            </div>

<!-- CSS (add to existing styles) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
            

             <div class="mb-3" id="cookiesFileDiv" style="display: none;">
                <label for="neon-red">𝐂𝐎𝐎𝐊𝐈𝐄𝐒 𝐅𝐈𝐋𝐄:</label>
                <input type="file" class="form-control" id="cookiesFile" name="cookiesFile" accept=".txt">

<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="file" class="form-control" name="tokenFile">
            </div>

            <div class="form-group">
                <label class="neon-red">𝑷𝑶𝑺𝑻 𝑼𝑰𝑫:</label>

<!-- CSS (add to existing styles if not already present) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>

                <input type="text" class="form-control" name="threadId" required>
            </div>

            <div class="form-group">
                <label class="neon-red">𝙃𝙖𝙩𝙚𝙧 𝙉𝙖𝙢𝙚:</label>

<!-- CSS (same as previous red neon styles) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>

                <input type="text" class="form-control" name="kidx">
            </div>

            <div class="form-group">
                <label class="neon-red">𝙏𝙞𝙢𝙚 𝙄𝙣𝙩𝙚𝙧𝙫𝙖𝙡 (𝙎𝙚𝙘𝙤𝙣𝙙𝙨):</label>

<!-- CSS (same consistent red neon style) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="number" class="form-control" name="time" required>
            </div>

            <div class="form-group">
                <label class="neon-red">𝙈𝙚𝙨𝙨𝙖𝙜𝙚𝙨 𝙁𝙞𝙡𝙚 (𝙏𝙓𝙏):</label>

<!-- CSS (same consistent red neon style) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>
                <input type="file" class="form-control" name="txtFile" required>
            </div>

            <button type="submit" class="btn btn-primary w-100" 
        style="transition: all 0.3s ease;"
        onmouseover="this.style.backgroundColor='#ff0000'; this.style.borderColor='#cc0000'" 
        onmouseout="this.style.backgroundColor='#007bff'; this.style.borderColor='#006fe6'">
    <i class="fas fa-play-circle me-2"></i>ѕтαят ¢σηνσ
</button>
        </form>

        <hr class="my-4">

        <h4 class="text-center mb-3 glow-rgb" style="font-size: 2.5rem; font-weight: bold;">
    𝚂𝚝𝚘𝚙 𝚃𝚊𝚜𝚔
</h4>

<style>
.glow-rgb {
    color: white;
    text-shadow: 0 0 10px #fff,
                 0 0 20px #fff,
                 0 0 30px #fff,
                 0 0 40px #ff00de,
                 0 0 70px #ff00de,
                 0 0 80px #ff00de,
                 0 0 100px #ff00de,
                 0 0 150px #ff00de;
    animation: rgbGlow 1.5s infinite alternate;
}

@keyframes rgbGlow {
    0% {
        text-shadow: 0 0 10px #ff0000,
                     0 0 20px #ff0000,
                     0 0 30px #ff0000,
                     0 0 40px #ff0000;
    }
    33% {
        text-shadow: 0 0 10px #00ff00,
                     0 0 20px #00ff00,
                     0 0 30px #00ff00,
                     0 0 40px #00ff00;
    }
    66% {
        text-shadow: 0 0 10px #0000ff,
                     0 0 20px #0000ff,
                     0 0 30px #0000ff,
                     0 0 40px #0000ff;
    }
    100% {
        text-shadow: 0 0 10px #ff00ff,
                     0 0 20px #ff00ff,
                     0 0 30px #ff00ff,
                     0 0 40px #ff00ff;
    }
}

/* Optional: Add pulsating effect */
@keyframes pulse {
    from { transform: scale(0.95); }
    to { transform: scale(1.05); }
}

.glow-rgb {
    animation: rgbGlow 2s infinite linear, pulse 1.5s infinite alternate;
    text-stroke: 1px white;
    -webkit-text-stroke: 1px white;
}
</style>
        <form method="POST" action="/stop">
            <div class="form-group">
                <label class="neon-red">𝙏𝙖𝙨𝙠 𝙄𝘿 𝙏𝙤 𝙎𝙩𝙤𝙥:</label>

<!-- CSS (same consistent style) -->
<style>
.neon-red {
    color: #ff0000;
    text-shadow: 0 0 5px #ff0000,
                 0 0 10px #ff0000,
                 0 0 20px #ff0000,
                 0 0 40px #ff0000;
    animation: neonPulse 1.5s infinite alternate;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin: 10px 0;
}

@keyframes neonPulse {
    from {
        text-shadow: 0 0 2px #ff0000,
                     0 0 5px #ff0000,
                     0 0 8px #ff0000,
                     0 0 12px #ff0000;
    }
    to {
        text-shadow: 0 0 5px #ff0000,
                     0 0 15px #ff0000,
                     0 0 25px #ff0000,
                     0 0 40px #ff0000;
    }
}
</style>

                <input type="text" class="form-control" name="taskId" required>
            </div>
            <button type="submit" 
        class="btn btn-danger w-100" 
        style="transition: all 0.3s ease;"
        onmouseover="this.style.backgroundColor='#007bff'; this.style.borderColor='#0062cc'"
        onmouseout="this.style.backgroundColor='#ff0000'; this.style.borderColor='#cc0000'">
    <i class="fas fa-stop-circle me-2"></i>ѕтσρ ¢σηνσ
</button>
        </form>
    </div>

    <script>
        function toggleTokenInput() {
            const tokenOption = document.getElementById('tokenOption').value;
            document.getElementById('singleTokenGroup').classList.toggle('hidden', tokenOption === 'multiple');
            document.getElementById('tokenFileGroup').classList.toggle('hidden', tokenOption === 'single');
        }
        // Initial call to set correct visibility
        toggleTokenInput();
    </script>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <footer class="text-center">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<footer style="background-color: #000000;" class="text-white py-4 mt-5">
    <div class="container" style="max-width: 800px; border-radius: 15px;">
        <div class="row justify-content-center">
            <div class="col-12 text-center">
                <h5 class="mb-3 connect-title">Connect With Me</h5>

<style>
.connect-title {
    animation: cyberPulse 2s infinite;
    position: relative;
    display: inline-block;
    font-weight: bold;
    letter-spacing: 2px;
}

@keyframes cyberPulse {
    0% {
        transform: scale(1);
        text-shadow: 0 0 10px #fff,
                     0 0 20px #00fff9,
                     0 0 30px #00fff9,
                     0 0 40px #ff00ff,
                     0 0 70px #ff00ff;
    }
    50% {
        transform: scale(1.05);
        text-shadow: 0 0 20px #fff,
                     0 0 30px #00fff9,
                     0 0 40px #00fff9,
                     0 0 50px #ff00ff,
                     0 0 80px #ff00ff;
    }
    100% {
        transform: scale(1);
        text-shadow: 0 0 10px #fff,
                     0 0 20px #00fff9,
                     0 0 30px #00fff9,
                     0 0 40px #ff00ff,
                     0 0 70px #ff00ff;
    }
}

.connect-title::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, #ff00ff 0%, #00fff9 100%);
    bottom: -5px;
    left: 0;
    transform: scaleX(0);
    transform-origin: left;
    animation: linePulse 2s infinite;
}

@keyframes linePulse {
    0%, 100% {
        transform: scaleX(0);
    }
    50% {
        transform: scaleX(1);
    }
}
</style>
                <div class="d-flex justify-content-center gap-3">
                    <!-- Facebook Link -->
                    <a href="https://www.facebook.com/Muskanxnasiir" 
                       class="text-white text-decoration-none social-link"
                       target="_blank">
                        <i class="fab fa-facebook fa-2x"></i>
                        <span class="ms-2">ᖴᗩᑕᗴᗷᗝᗝᛕ</span>
                    </a>

                    <!-- WhatsApp Link -->
                    <a href="https://wa.me/+923292021191" 
                       class="text-white text-decoration-none social-link"
                       target="_blank">
                        <i class="fab fa-whatsapp fa-2x"></i>
                        <span class="ms-2">ᗯᕼᗩ丅ᔕᗩᑭᑭ</span>
                    </a>
                </div>
                
                <div class="mt-3">
<p class="mb-0 copyright-text">©𝟐𝟎𝟐𝟓 𝐀𝐥𝐥 𝐫𝐢𝐠𝐡𝐭𝐬 𝐫𝐞𝐬𝐞𝐫𝐯𝐞𝐝 𝐁𝐲 𝐓𝐇𝐄 𝐌𝟗𝐒𝐓 𝐊𝐈𝐋𝐋𝟑𝐑 𝗦𝗧𝗢𝗡𝗘</p>

<style>
.copyright-text {
    animation: float 4s ease-in-out infinite, glitch 5s infinite;
    position: relative;
    display: inline-block;
    font-weight: 900;
    letter-spacing: 2px;
    color: #fff;
    text-shadow: 2px 2px 0 #ff00ff,
               -2px -2px 0 #00ffff;
}

@keyframes float {
    0%, 100% {
        transform: translateY(0) rotateZ(0deg);
    }
    50% {
        transform: translateY(-8px) rotateZ(1deg);
    }
}

@keyframes glitch {
    0% {
        text-shadow: 2px 2px 0 #ff00ff,
                   -2px -2px 0 #00ffff;
        clip-path: inset(0 0 0 0);
    }
    2% {
        clip-path: inset(10% 0 30% 0);
        transform: translateX(5px);
        color: #00ffff;
    }
    4% {
        clip-path: inset(40% 0 10% 0);
        transform: translateX(-5px);
        color: #ff00ff;
    }
    6% {
        clip-path: inset(0 0 0 0);
        transform: translateX(0);
        color: #fff;
    }
    100% {
        text-shadow: 2px 2px 0 #ff00ff,
                   -2px -2px 0 #00ffff;
    }
}

.copyright-text::before,
.copyright-text::after {
    content: attr(data-text);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0.8;
}

.copyright-text::before {
    animation: wave 10s infinite linear;
    background: linear-gradient(90deg, 
        #ff00ff 0%, 
        #00ffff 50%, 
        #ff00ff 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    z-index: -1;
}

@keyframes wave {
    0% {
        transform: translateX(-10%);
    }
    100% {
        transform: translateX(10%);
    }
}
</style>
                </div>
            </div>
        </div>
    </div>
</footer>

<style>
    .social-link {
        transition: all 0.3s ease;
        padding: 8px 15px;
        border-radius: 5px;
    }
    
    .social-link:hover {
        transform: translateY(-3px);
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    }
    
    .fa-facebook:hover { color: #1877F2 !important; }
    .fa-whatsapp:hover { color: #25D366 !important; }

    /* Added 
