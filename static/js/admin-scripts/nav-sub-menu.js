document.querySelectorAll('.nav-item').forEach(item => {
    const navItemButton = item.querySelector('button');
    const subMenu = item.querySelector('ul');

    navItemButton.addEventListener('click', () => {
        if (subMenu.classList.contains('h-0')) {
            subMenu.classList.remove('h-0');
        }
        else {
            subMenu.classList.add('h-0');
        }
    });
});