document.addEventListener("DOMContentLoaded", () => {
    const saludo = document.getElementById("saludo");
    const icono = document.getElementById("icono-perfil");

    if (!saludo || !icono) return;

    const hora = new Date().getHours();
    const colores = ["#0d6efd", "#dc3545", "#198754", "#ffc107", "#6f42c1", "#fd7e14"];
    const colorRandom = colores[Math.floor(Math.random() * colores.length)];

    let mensaje = "";
    if (hora < 12) mensaje = `buenos días ☀️`;
    else if (hora < 18) mensaje = `buenas tardes 🌤️`;
    else mensaje = `buenas noches 🌙`;

    saludo.textContent = mensaje;
    icono.style.color = colorRandom;
});

