document.addEventListener("DOMContentLoaded", () => {
    const saludo = document.getElementById("saludo");
    const icono = document.getElementById("icono-perfil");
    const textoEstado = document.getElementById("texto-estado");
    const iconoEstado = document.getElementById("icono-estado");
    let tiempoInactividad;

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

    // Función para marcar inactivo
    function marcarInactivo() {
        textoEstado.textContent = "Estado inactivo";
        iconoEstado.className = "bi bi-x-circle-fill text-danger";
    }

    // Función para resetear temporizador
    function resetearInactividad() {
        clearTimeout(tiempoInactividad);
        textoEstado.textContent = "Estado activo";
        iconoEstado.className = "bi bi-check-circle-fill text-success";
        tiempoInactividad = setTimeout(marcarInactivo, 15000); // 30 seg
    }

    // Detectar actividad
    window.onload = resetearInactividad;
    document.onmousemove = resetearInactividad;
    document.onkeypress = resetearInactividad;
    document.onscroll = resetearInactividad;
    document.onclick = resetearInactividad;
});

