// The Security Paradox - Interactive Elements

document.addEventListener('DOMContentLoaded', () => {
    console.log('The Security Paradox site loaded');

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Fade in elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe doorways and content items
    document.querySelectorAll('.doorway, .content-item, .model-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Add stagger delay to doorways
    document.querySelectorAll('.doorway').forEach((doorway, index) => {
        doorway.style.transitionDelay = `${index * 0.1}s`;
    });

    // Gentle pulse animation for hero on load
    const hero = document.querySelector('.hero-title');
    if (hero) {
        setTimeout(() => {
            hero.style.animation = 'gentlePulse 2s ease-in-out';
        }, 300);
    }
});