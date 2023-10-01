// Referências aos elementos HTML
const insereOpenPopupButton = document.getElementById('inserePopupOpen');
const insereClosePopupButton = document.getElementById('inserePopupClose');
const popup = document.getElementById('popup');
const overlay = document.createElement('div');
overlay.className = 'overlay';

// Abrir o popup
insereOpenPopupButton.addEventListener('click', () => {
    document.body.appendChild(overlay);
    popup.style.display = 'block';
});

// Fechar o popup
insereClosePopupButton.addEventListener('click', () => {
    document.body.removeChild(overlay);
    popup.style.display = 'none';
});
