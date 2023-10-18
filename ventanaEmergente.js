// script.js
document.addEventListener("DOMContentLoaded", function() {
    var btnMostrar = document.getElementById("btnMostrar");
    var miModal = document.getElementById("miModal");
    var cerrarModal = document.getElementById("cerrarModal");

    btnMostrar.addEventListener("click", function() {
        miModal.style.display = "block";
    });

    cerrarModal.addEventListener("click", function() {
        miModal.style.display = "none";
    });
});
