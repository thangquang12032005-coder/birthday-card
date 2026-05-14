from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="vi">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Happy Birthday</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{

    font-family:'Poppins',sans-serif;

    height:100vh;

    overflow:hidden;

    display:flex;
    justify-content:center;
    align-items:center;

    background:
    linear-gradient(
        135deg,
        #f4f7fb,
        #e8eef8,
        #f7fbff
    );

    position:relative;
}

/* background blur */

.bg1,
.bg2,
.bg3{

    position:absolute;

    border-radius:50%;

    filter:blur(100px);

    opacity:0.5;
}

.bg1{

    width:350px;
    height:350px;

    background:#cfe2ff;

    top:-100px;
    left:-100px;
}

.bg2{

    width:300px;
    height:300px;

    background:#ffd6e5;

    bottom:-100px;
    right:-50px;
}

.bg3{

    width:250px;
    height:250px;

    background:#dcfce7;

    top:50%;
    left:50%;

    transform:translate(-50%,-50%);
}

/* bánh kem bay */

.cakes{

    position:absolute;

    width:100%;
    height:100%;

    overflow:hidden;

    z-index:0;
}

.cake{

    position:absolute;

    bottom:-50px;

    opacity:0.85;

    animation:float 8s linear infinite;
}

@keyframes float{

    0%{

        transform:translateY(0) rotate(0deg) scale(1);

        opacity:0;
    }

    15%{
        opacity:1;
    }

    100%{

        transform:
        translateY(-120vh)
        rotate(20deg)
        scale(1.5);

        opacity:0;
    }
}

/* popup */

.popup{

    position:fixed;

    inset:0;

    background:rgba(255,255,255,0.2);

    backdrop-filter:blur(8px);

    display:flex;

    justify-content:center;
    align-items:center;

    z-index:100;
}

.popup-box{

    width:360px;

    background:white;

    border-radius:25px;

    padding:35px;

    text-align:center;

    box-shadow:
    0 10px 40px rgba(0,0,0,0.08);

    animation:fadeUp 0.6s ease;
}

.popup-box h2{

    color:#111827;

    margin-bottom:15px;

    font-size:30px;
}

.popup-box p{

    color:#6b7280;

    margin-bottom:25px;

    line-height:1.7;

    font-size:17px;
}

/* buttons */

.buttons{

    display:flex;

    justify-content:center;

    gap:15px;
}

button{

    border:none;

    padding:12px 24px;

    border-radius:14px;

    font-size:15px;

    font-weight:600;

    cursor:pointer;

    transition:0.3s;
}

.yes-btn{

    background:#111827;

    color:white;
}

.yes-btn:hover{

    transform:translateY(-3px);
}

.no-btn{

    background:#ffe4ec;

    color:#ff4f81;
}

/* main */

.main{

    text-align:center;

    z-index:2;

    display:none;
}

.main.show{

    display:block;
}

/* title */

.main-title{

    margin-bottom:35px;
}

.main-title h1{

    font-size:55px;

    color:#111827;

    font-weight:700;

    letter-spacing:2px;
}

.main-title p{

    color:#6b7280;

    margin-top:10px;

    font-size:18px;
}

/* envelope */

.envelope{

    position:relative;

    width:340px;
    height:230px;

    margin:auto;

    background:rgba(255,255,255,0.7);

    backdrop-filter:blur(14px);

    border-radius:24px;

    cursor:pointer;

    box-shadow:
    0 10px 40px rgba(0,0,0,0.08);

    overflow:visible;
}

/* flap */

.envelope::before{

    content:'';

    position:absolute;

    top:0;
    left:0;

    width:0;
    height:0;

    border-left:170px solid transparent;
    border-right:170px solid transparent;
    border-top:115px solid #dbeafe;

    transform-origin:top;

    transition:1s;

    z-index:4;
}

/* open */

.envelope.open::before{

    transform:rotateX(180deg);
}

/* letter */

.letter{

    position:absolute;

    left:20px;
    top:25px;

    width:300px;
    height:180px;

    background:white;

    border-radius:20px;

    padding:25px;

    box-shadow:
    0 8px 25px rgba(0,0,0,0.05);

    transition:1s;

    transform:translateY(50px);

    opacity:0;

    z-index:10;
}

.envelope.open .letter{

    transform:translateY(-120px);

    opacity:1;
}

/* text */

.letter h2{

    font-size:30px;

    color:#111827;

    margin-bottom:18px;
}

.letter p{

    color:#4b5563;

    font-size:17px;

    line-height:1.8;
}

/* click */

.click-text{

    margin-top:25px;

    color:#6b7280;

    font-size:15px;

    animation:pulse 2s infinite;
}

/* credit */

.credit{

    position:fixed;

    bottom:20px;

    width:100%;

    text-align:center;

    color:#6b7280;

    font-size:15px;

    font-weight:500;

    z-index:10;
}

.credit span{

    color:#111827;

    font-weight:700;
}

@keyframes pulse{

    0%{
        opacity:0.4;
    }

    50%{
        opacity:1;
    }

    100%{
        opacity:0.4;
    }
}

@keyframes fadeUp{

    from{

        opacity:0;

        transform:translateY(40px);
    }

    to{

        opacity:1;

        transform:translateY(0);
    }
}

/* mobile */

@media(max-width:600px){

    .popup-box{
        width:90%;
    }

    .main-title h1{
        font-size:38px;
    }

    .envelope{
        width:300px;
        height:210px;
    }

    .envelope::before{

        border-left:150px solid transparent;
        border-right:150px solid transparent;
        border-top:100px solid #dbeafe;
    }

    .letter{

        width:260px;
        height:170px;
    }

    .letter h2{
        font-size:24px;
    }

    .letter p{
        font-size:15px;
    }

    .credit{
        font-size:13px;
    }
}

</style>
</head>

<body>

<div class="bg1"></div>
<div class="bg2"></div>
<div class="bg3"></div>

<!-- bánh kem bay -->

<div class="cakes" id="cakes"></div>

<!-- popup chính -->

<div class="popup" id="popup">

    <div class="popup-box">

        <h2>🎂 Happy Birthday 🎂</h2>

        <p>
            Bạn có muốn đọc bức thư dành riêng
            cho Quảng Trọng Ngọc không? 💌
        </p>

        <div class="buttons">

            <button class="yes-btn"
            onclick="openLetter()">

                Có 💖

            </button>

            <button class="no-btn"
            onclick="showSadPopup()">

                Không 🥺

            </button>

        </div>

    </div>

</div>

<!-- popup buồn -->

<div class="popup"
id="sadPopup"
style="display:none;">

    <div class="popup-box">

        <h2 style="font-size:70px;">
            😭
        </h2>

        <p>
            Đừng mà...
            <br><br>
            Người ta chuẩn bị bức thư này
            lâu lắm luôn đó 💔
        </p>

        <div class="buttons">

            <button class="yes-btn"
            onclick="backPopup()">

                Quay lại mở thư 💌

            </button>

        </div>

    </div>

</div>

<!-- main -->

<div class="main" id="mainContent">

    <div class="main-title">

        <h1>🎉 QUẢNG TRỌNG NGỌC 🎉</h1>

        <p>
            Chúc mừng sinh nhật ✨
        </p>

    </div>

    <div class="envelope" id="envelope">

        <div class="letter">

            <h2>Happy Birthday 🎂</h2>

            <p>
                Chúc em tuổi mới lúc nào cũng
                nhiều năng lượng tích cực
                và luôn được cưng chiều nha 💖
            </p>

        </div>

    </div>

    <div class="click-text">
        💌 Nhấn để mở thư 💌
    </div>

</div>

<!-- credit -->

<div class="credit">

    Người làm thiệp :
    <span>Trương Quang Nhị</span> 💖

</div>

<script>

/* mở thư */

function openLetter(){

    document.getElementById("popup").style.display = "none";

    document.getElementById("sadPopup").style.display = "none";

    document.getElementById("mainContent")
    .classList.add("show");
}

/* popup buồn */

function showSadPopup(){

    document.getElementById("popup").style.display = "none";

    document.getElementById("sadPopup").style.display = "flex";
}

/* quay lại */

function backPopup(){

    document.getElementById("sadPopup").style.display = "none";

    document.getElementById("popup").style.display = "flex";
}

/* envelope */

const envelope = document.getElementById("envelope");

envelope.addEventListener("click",()=>{

    envelope.classList.toggle("open");

});

/* bánh kem bay */

const cakes = document.getElementById("cakes");

function createCake(){

    const cake = document.createElement("div");

    cake.classList.add("cake");

    cake.innerHTML = "🎂";

    cake.style.left =
        Math.random()*100 + "vw";

    cake.style.fontSize =
        (Math.random()*20 + 20) + "px";

    cake.style.animationDuration =
        (Math.random()*4 + 5) + "s";

    cakes.appendChild(cake);

    setTimeout(()=>{
        cake.remove();
    },9000);
}

setInterval(createCake,500);

</script>

</body>
</html>
"""

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)