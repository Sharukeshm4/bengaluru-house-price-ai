// Parallax tilt
document.addEventListener("mousemove", e => {
    const x = (e.clientX / window.innerWidth - 0.5) * 20;
    const y = (e.clientY / window.innerHeight - 0.5) * 20;

    document.getElementById("card").style.transform =
        `translate(-50%, -50%) rotateY(${x}deg) rotateX(${-y}deg)`;
});

// Price counter animation
const price = document.getElementById("price");
if (price) {
    let value = price.innerText.replace(/[^\d.]/g, "");
    let current = 0;
    let interval = setInterval(() => {
        current += value / 30;
        price.innerText = "₹ " + current.toFixed(2) + " Lakhs";
        if (current >= value) clearInterval(interval);
    }, 30);
}

function startAI() {
    document.body.style.filter = "brightness(1.1)";
}
