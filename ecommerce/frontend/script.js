// URL de l'API Django
const API_URL = "http://127.0.0.1:8000/api/products";

// Fonction pour récupérer les produits depuis l'API
async function fetchProducts() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const products = await response.json();
        displayProducts(products);
    } catch (error) {
        console.error("Erreur lors du chargement des produits :", error);
    }
}

// Fonction pour afficher les produits dans le DOM
function displayProducts(products) {
    const productList = document.getElementById("product-list");

    products.forEach((product) => {
        const productCard = document.createElement("div");
        productCard.className = "product-card";

        productCard.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <div class="info">
                <h2>${product.name}</h2>
                <p>${product.description}</p>
                <p class="price">Prix : ${product.price} FCFA</p>
                <p>Prix minimum : ${product.min_price} FCFA</p>
                <a href="${product.video}" target="_blank">Voir la vidéo</a>
            </div>
        `;

        productList.appendChild(productCard);
    });
}

// Charger les produits lors du chargement de la page
document.addEventListener("DOMContentLoaded", fetchProducts);
