function toggleMenu(caret) {
    var parent = caret.parentElement;
    var nestedMenu = parent.querySelector('.nested');
    nestedMenu.style.display = (nestedMenu.style.display === 'block') ? 'none' : 'block';
}