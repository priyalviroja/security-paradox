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

    // Doorway toggle functionality - ONE AT A TIME
    const doorwayToggles = document.querySelectorAll('.doorway-toggle');
    const allColumns = document.querySelectorAll('.content-column');

    doorwayToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault();

            const targetId = toggle.getAttribute('data-target');
            const targetColumn = document.getElementById(targetId);

            if (!targetColumn) return;

            // Check if this column is currently the only one visible
            const isCurrentlyActive = toggle.classList.contains('active');
            const activeCount = document.querySelectorAll('.doorway-toggle.active').length;
            const isOnlyActive = isCurrentlyActive && activeCount === 1;

            if (isOnlyActive) {
                // If clicking the only active column, show all columns
                doorwayToggles.forEach(t => {
                    t.classList.add('active');
                    const indicator = t.querySelector('.doorway-indicator');
                    if (indicator) indicator.textContent = '−';
                });

                allColumns.forEach(col => {
                    col.classList.remove('hidden');
                });
            } else {
                // Hide all other columns, show only this one
                doorwayToggles.forEach(t => {
                    if (t === toggle) {
                        t.classList.add('active');
                        const indicator = t.querySelector('.doorway-indicator');
                        if (indicator) indicator.textContent = '−';
                    } else {
                        t.classList.remove('active');
                        const indicator = t.querySelector('.doorway-indicator');
                        if (indicator) indicator.textContent = '+';
                    }
                });

                allColumns.forEach(col => {
                    if (col === targetColumn) {
                        col.classList.remove('hidden');
                    } else {
                        col.classList.add('hidden');
                    }
                });

                // Smooth scroll to the revealed column
                setTimeout(() => {
                    targetColumn.scrollIntoView({
                        behavior: 'smooth',
                        block: 'nearest'
                    });
                }, 300);
            }
        });
    });

    // Journey circle node clicks
    const journeyNodes = document.querySelectorAll('.journey-node');
    journeyNodes.forEach(node => {
        node.addEventListener('click', (e) => {
            const href = node.getAttribute('data-href');
            if (href) {
                window.location.href = href;
            }
        });
    });

    // List view toggle
    const toggleBtn = document.getElementById('toggleListView');
    const listView = document.getElementById('journeyListView');

    if (toggleBtn && listView) {
        toggleBtn.addEventListener('click', () => {
            const isVisible = listView.style.display !== 'none';

            if (isVisible) {
                listView.style.display = 'none';
                toggleBtn.querySelector('.toggle-text').textContent = 'Show List View';
                toggleBtn.querySelector('.toggle-icon').textContent = '📋';
            } else {
                listView.style.display = 'block';
                toggleBtn.querySelector('.toggle-text').textContent = 'Hide List View';
                toggleBtn.querySelector('.toggle-icon').textContent = '✕';

                // Smooth scroll to list view
                setTimeout(() => {
                    listView.scrollIntoView({
                        behavior: 'smooth',
                        block: 'nearest'
                    });
                }, 100);
            }
        });
    }
});