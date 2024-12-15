// Ініціалізація карти
const map = L.map('map').setView([49.8397, 24.0297], 8); // Координати Львова

// Додавання OpenStreetMap шару
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(map);

// Додавання маркерів для прикладу
L.marker([49.6297, 23.9305]).addTo(map)
    .bindPopup('Річка Дністер, стан: Задовільний');
L.marker([49.2583, 23.8542]).addTo(map)
    .bindPopup('Річка Стрий, стан: Незадовільний');
L.marker([50.1071, 24.3466]).addTo(map)
    .bindPopup('Західний Буг, стан: Добрий');
