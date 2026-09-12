document.addEventListener('DOMContentLoaded', function() {
    const pathname = document.location.pathname;
    const portfolioLink = document.querySelector('#portfolio');
    const indexLink = document.querySelector('#index');

    if (pathname === '/') {
        indexLink.classList.add('active');
        portifolioLink.classList.remove('active');
    } else if (pathname === '/portfolio/') {
        portfolioLink.classList.add('active');
        indexLink.classList.remove('active');
    }
});