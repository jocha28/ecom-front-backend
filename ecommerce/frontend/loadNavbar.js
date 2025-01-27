document.addEventListener("DOMContentLoaded", function() {
    // Récupérer l'élément avec id "navbar"
    const navbar = document.getElementById("navbar");

    // Charger le contenu de navbar.html
    fetch("navbar.html")
        .then(response => response.text())
        .then(data => {
            navbar.innerHTML = data;
        })
        .catch(error => {
            console.error("Erreur lors du chargement de la barre de navigation :", error);
        });
});
