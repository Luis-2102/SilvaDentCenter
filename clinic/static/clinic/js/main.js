// ============ LOADING SCREEN ============
document.addEventListener('DOMContentLoaded', function () {
    // Hide loading screen after animation
    setTimeout(function () {
        const loadingScreen = document.getElementById('loadingScreen');
        if (loadingScreen) {
            loadingScreen.classList.add('hidden');
        }
    }, 2500);

    // Initialize all components
    initHeader();
    initMobileMenu();
    initRevealAnimations();
    initCounterAnimations();
    initCarousel();
    initModals();
    initSpecialtyCardHandlers();
    initWorksGalleryImages();
    initActiveNavTracking();
});

// ============ HEADER ============
function initHeader() {
    const header = document.getElementById('siteHeader');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 30) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
}

// ============ MOBILE MENU ============
function initMobileMenu() {
    const burgerBtn = document.getElementById('burgerBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    const mobileOverlay = document.getElementById('mobileOverlay');
    const mmClose = document.getElementById('mmClose');

    function openMenu() {
        mobileMenu.classList.add('open');
        mobileOverlay.classList.add('show');
        document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
        mobileMenu.classList.remove('open');
        mobileOverlay.classList.remove('show');
        document.body.style.overflow = '';
    }

    if (burgerBtn) {
        burgerBtn.addEventListener('click', openMenu);
    }

    if (mmClose) {
        mmClose.addEventListener('click', closeMenu);
    }

    if (mobileOverlay) {
        mobileOverlay.addEventListener('click', closeMenu);
    }

    const mobileLinks = mobileMenu ? mobileMenu.querySelectorAll('a') : [];
    mobileLinks.forEach(function (link) {
        link.addEventListener('click', closeMenu);
    });
}

// ============ REVEAL ANIMATIONS ============
function initRevealAnimations() {
    const revealElements = document.querySelectorAll('.reveal');

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15 });

    revealElements.forEach(function (el) {
        observer.observe(el);
    });
}

// ============ COUNTER ANIMATIONS ============
function initCounterAnimations() {
    const counters = document.querySelectorAll('[data-count]');

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseInt(el.getAttribute('data-count'), 10);
                let current = 0;
                const step = Math.max(1, Math.ceil(target / 60));

                const tick = function () {
                    current += step;
                    if (current >= target) {
                        el.textContent = target.toString();
                        return;
                    }
                    el.textContent = current.toString();
                    requestAnimationFrame(tick);
                };

                tick();
                observer.unobserve(el);
            }
        });
    }, { threshold: 0.6 });

    counters.forEach(function (el) {
        observer.observe(el);
    });
}

// ============ CAROUSEL ============
let carouselIndex = 0;
let visibleCards = 3;

function initCarousel() {
    updateVisibleCards();
    window.addEventListener('resize', updateVisibleCards);

    const prevBtn = document.getElementById('carouselPrev');
    const nextBtn = document.getElementById('carouselNext');

    if (prevBtn) {
        prevBtn.addEventListener('click', function () {
            if (carouselIndex > 0) {
                carouselIndex--;
                updateCarousel();
            }
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function () {
            const track = document.getElementById('carouselTrack');
            if (track) {
                const cards = track.querySelectorAll('.testi-card');
                const maxIndex = cards.length - visibleCards;
                if (carouselIndex < maxIndex) {
                    carouselIndex++;
                    updateCarousel();
                }
            }
        });
    }
}

function updateVisibleCards() {
    if (window.innerWidth < 768) {
        visibleCards = 1;
    } else if (window.innerWidth < 1100) {
        visibleCards = 2;
    } else {
        visibleCards = 3;
    }
    updateCarousel();
}

function updateCarousel() {
    const track = document.getElementById('carouselTrack');
    if (track) {
        const translateX = carouselIndex * (100 / visibleCards);
        track.style.transform = 'translateX(-' + translateX + '%)';
    }
}

// ============ MODALS ============
function initModals() {
    // Close modals on overlay click
    const modals = document.querySelectorAll('.modal-overlay');
    modals.forEach(function (modal) {
        modal.addEventListener('click', function (e) {
            if (e.target === modal) {
                modal.classList.remove('open');
                document.body.style.overflow = '';
            }
        });
    });
}

function initSpecialtyCardHandlers() {
    const cards = document.querySelectorAll('[data-specialty-id]');

    cards.forEach(function (card) {
        card.addEventListener('click', function (event) {
            const specialtyId = parseInt(this.getAttribute('data-specialty-id'), 10);
            if (!Number.isNaN(specialtyId)) {
                openSpecialtyDetail(specialtyId);
            }
        });
    });
}

function initWorksGalleryImages() {
    const images = document.querySelectorAll('.gallery-work-image');

    images.forEach(function (img) {
        const media = img.closest('.gallery-media');

        if (!media) {
            return;
        }

        const markLoaded = function () {
            media.classList.remove('is-loading');
            media.classList.add('is-loaded');
            img.classList.add('is-visible');
        };

        if (img.complete && img.naturalWidth > 0) {
            markLoaded();
            return;
        }

        img.addEventListener('load', markLoaded, { once: true });
        img.addEventListener('error', markLoaded, { once: true });
    });
}

function openSpecialtiesModal() {
    const modal = document.getElementById('specialtiesModal');
    if (modal) {
        modal.classList.add('open');
        document.body.style.overflow = 'hidden';
    }
}

function closeSpecialtiesModal() {
    const modal = document.getElementById('specialtiesModal');
    if (modal) {
        modal.classList.remove('open');
        document.body.style.overflow = '';
    }
}

function openSpecialtyDetail(specialtyId) {
    const modal = document.getElementById('specialtyDetailModal');
    const content = document.getElementById('specialtyDetailContent');

    if (!modal || !content) return;

    content.innerHTML = '<div class="specialty-detail-loading" style="padding:40px;text-align:center;color:var(--slate);">Cargando especialidad...</div>';
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';

    const url = (window.specialtyDetailUrlBase || '/especialidad/') + specialtyId + '/';

    fetch(url, {
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
    })
        .then(function (response) {
            if (!response.ok) {
                throw new Error('No se pudo cargar la especialidad');
            }
            return response.text();
        })
        .then(function (html) {
            content.innerHTML = html;
        })
        .catch(function () {
            content.innerHTML = '<div class="specialty-detail-loading" style="padding:40px;text-align:center;color:var(--slate);">No se pudo cargar la información de la especialidad.</div>';
        });
}

function closeSpecialtyDetailModal() {
    const modal = document.getElementById('specialtyDetailModal');
    if (modal) {
        modal.classList.remove('open');
        document.body.style.overflow = '';
    }
}

function openWorksModal() {
    const modal = document.getElementById('worksModal');
    const grid = document.getElementById('worksGalleryGrid');

    if (!modal) {
        return;
    }

    modal.classList.add('open');
    document.body.style.overflow = 'hidden';

    if (!grid) {
        return;
    }

    grid.innerHTML = '<div class="gallery-loading">Cargando trabajos...</div>';

    fetch('/trabajos/', {
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
    })
        .then(function (response) {
            if (!response.ok) {
                throw new Error('No se pudieron cargar los trabajos');
            }
            return response.json();
        })
        .then(function (data) {
            if (!Array.isArray(data.works)) {
                throw new Error('Formato inválido');
            }

            if (data.works.length === 0) {
                grid.innerHTML = '<div class="gallery-empty">No hay trabajos disponibles.</div>';
                return;
            }

            grid.innerHTML = data.works.map(function (work) {
                const imageMarkup = work.image_url
                    ? '<div class="gallery-media is-loading"><img src="' + work.image_url + '" alt="' + work.title.replace(/"/g, '&quot;') + '" loading="lazy" class="gallery-work-image"></div>'
                    : '';

                return '<div class="gallery-item">' + imageMarkup + '<div class="gallery-overlay"><h4>' + work.title + '</h4><span>' + work.procedure + '</span></div></div>';
            }).join('');

            initWorksGalleryImages();
        })
        .catch(function () {
            grid.innerHTML = '<div class="gallery-empty">No se pudieron cargar los trabajos.</div>';
        });
}

function closeWorksModal() {
    const modal = document.getElementById('worksModal');
    if (modal) {
        modal.classList.remove('open');
        document.body.style.overflow = '';
    }
}

// ============ ACTIVE NAV TRACKING ============
function initActiveNavTracking() {
    const sections = ['inicio', 'nosotros', 'servicios', 'contactos'];
    const navLinks = document.querySelectorAll('.nav-links a');

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(function (link) {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + id) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, { rootMargin: '-45% 0px -45% 0px' });

    sections.forEach(function (id) {
        const el = document.getElementById(id);
        if (el) {
            observer.observe(el);
        }
    });
}

// ============ WHATSAPP ============
function openWhatsApp() {
    const message = encodeURIComponent('Hola👋, me gustaría agendar una cita en SILVADENT CENTER. Espero su confirmacion.');
    window.open('https://wa.me/' + WHATSAPP_NUMBER + '?text=' + message, '_blank');
}

// ============ FORM SUBMISSION ============
function handleFormSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const name = formData.get('name');
    const phone = formData.get('phone');
    const email = formData.get('email');
    const service = formData.get('service');
    const datetime = formData.get('datetime');

    // Build WhatsApp message
    const message = encodeURIComponent(
        'Hola, quisiera agendar una cita para ' + name + ', en la especialidad de ' + (service || 'evaluacion general') + ', para el dia: ' + (datetime || 'a definir') + ', en lo posible. Espero su confirmacion.'
    );

    // Open WhatsApp
    window.open('https://wa.me/' + WHATSAPP_NUMBER + '?text=' + message, '_blank');

    // Show success message
    const successEl = document.getElementById('formSuccess');
    if (successEl) {
        successEl.classList.add('show');
        form.reset();

        setTimeout(function () {
            successEl.classList.remove('show');
        }, 6000);
    }
}

