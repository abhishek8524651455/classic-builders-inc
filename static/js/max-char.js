const serviceCards = document.querySelectorAll('.service-card');

serviceCards.forEach(card => {
    const text = card.querySelector('.service-card-text');
    // text.innerHTML = text.innerHTML.slice(0, 16) + "...";
    text.innerHTML = text.innerHTML.slice(0, 159) + " [...]";
    console.log(serviceCards);
});
