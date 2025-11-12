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

    // Full-Screen Doorway Portal Functionality
    const doorwayPortals = document.querySelectorAll('.doorway-portal');
    const fullscreenDoorways = document.querySelector('.fullscreen-doorways');
    const expandedContent = document.querySelector('.expanded-content');
    const backButton = document.querySelector('.back-to-doorways');
    const doorwayContents = document.querySelectorAll('.doorway-content');

    function openDoorway(doorwayType) {
        // Hide the doorways section
        if (fullscreenDoorways) {
            fullscreenDoorways.classList.add('hidden');
        }

        // Show the expanded content section
        if (expandedContent) {
            expandedContent.classList.add('active');
        }

        // Show the specific content
        doorwayContents.forEach(content => {
            content.classList.remove('active');
        });

        const targetContent = document.getElementById(`${doorwayType}-content`);
        if (targetContent) {
            targetContent.classList.add('active');
        }

        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Enter doorway - attach to buttons
    doorwayPortals.forEach(portal => {
        const enterButton = portal.querySelector('.portal-enter');
        if (enterButton) {
            enterButton.addEventListener('click', (e) => {
                e.stopPropagation();
                const doorwayType = portal.getAttribute('data-doorway');
                openDoorway(doorwayType);
            });
        }

        // Also allow clicking the whole portal
        portal.addEventListener('click', () => {
            const doorwayType = portal.getAttribute('data-doorway');
            openDoorway(doorwayType);
        });
    });

    // Back to doorways
    if (backButton) {
        backButton.addEventListener('click', () => {
            // Hide expanded content
            if (expandedContent) {
                expandedContent.classList.remove('active');
            }

            // Hide all doorway contents
            doorwayContents.forEach(content => {
                content.classList.remove('active');
            });

            // Show doorways section
            if (fullscreenDoorways) {
                fullscreenDoorways.classList.remove('hidden');
            }

            // Scroll to doorways
            setTimeout(() => {
                if (fullscreenDoorways) {
                    fullscreenDoorways.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }, 100);
        });
    }

    // ESC key to return to doorways
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && expandedContent && expandedContent.classList.contains('active')) {
            backButton.click();
        }
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