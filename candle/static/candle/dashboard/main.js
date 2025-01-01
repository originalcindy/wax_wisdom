function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    const menuToggle = document.querySelector('.menu-toggle');
    
    sidebar.classList.toggle('active');
    
    // update aria-expanded state for accessibility
    const isExpanded = sidebar.classList.contains('active');
    menuToggle.setAttribute('aria-expanded', isExpanded);
}

// close sidebar when clicking outside
document.addEventListener('click', (e) => {
    const sidebar = document.querySelector('.sidebar');
    const menuToggle = document.querySelector('.menu-toggle');
    
    if (!sidebar.contains(e.target) && !menuToggle.contains(e.target) && sidebar.classList.contains('active')) {
        sidebar.classList.remove('active');
        menuToggle.setAttribute('aria-expanded', 'false');
    }
});

// handle window resize
window.addEventListener('resize', () => {
    const sidebar = document.querySelector('.sidebar');
    const menuToggle = document.querySelector('.menu-toggle');
    
    if (window.innerWidth > 768 && sidebar.classList.contains('active')) {
        sidebar.classList.remove('active');
        menuToggle.setAttribute('aria-expanded', 'false');
    }
});