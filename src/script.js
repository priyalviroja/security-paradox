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

    // Doorway toggle functionality
    const doorwayToggles = document.querySelectorAll('.doorway-toggle');

    doorwayToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault();

            const targetId = toggle.getAttribute('data-target');
            const targetColumn = document.getElementById(targetId);

            if (!targetColumn) return;

            // Toggle active state
            const isActive = toggle.classList.contains('active');

            if (isActive) {
                // Hide column
                toggle.classList.remove('active');
                targetColumn.classList.add('hidden');

                // Change indicator to +
                const indicator = toggle.querySelector('.doorway-indicator');
                if (indicator) indicator.textContent = '+';
            } else {
                // Show column
                toggle.classList.add('active');
                targetColumn.classList.remove('hidden');

                // Change indicator to −
                const indicator = toggle.querySelector('.doorway-indicator');
                if (indicator) indicator.textContent = '−';
            }

            // Smooth scroll to content section if revealing
            if (!isActive) {
                setTimeout(() => {
                    targetColumn.scrollIntoView({
                        behavior: 'smooth',
                        block: 'nearest'
                    });
                }, 300);
            }
        });
    });
});