// initialize header scroll effect
window.addEventListener('scroll', () => {
   const header = document.querySelector('header');
   if (window.scrollY > 100) {
       header.classList.add('scrolled');
   } else {
       header.classList.remove('scrolled');
   }
});

// smooth scroll for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
   anchor.addEventListener('click', function (e) {
       e.preventDefault();
       const target = document.querySelector(this.getAttribute('href'));
       if (target) {
           target.scrollIntoView({
               behavior: 'smooth',
               block: 'start'
           });
       }
   });
});
function toggleProfileMenu() {
   const trigger = document.querySelector('.profile-trigger');
   const menu = document.getElementById('profileMenu');
   
   trigger.classList.toggle('active');
   menu.classList.toggle('show');
   
   // close menu when clicking outside
   document.addEventListener('click', function(event) {
       const isClickInside = trigger.contains(event.target) || menu.contains(event.target);
       
       if (!isClickInside && menu.classList.contains('show')) {
           trigger.classList.remove('active');
           menu.classList.remove('show');
       }
   });
}
document.addEventListener('DOMContentLoaded', function() {
   const messages = document.querySelectorAll('.message');
   messages.forEach(message => {
       setTimeout(() => {
           message.remove();
       }, 5300);
   });
});
function toggleMobileMenu() {
   const navContainer = document.querySelector('.nav-container');
   const overlay = document.querySelector('.mobile-menu-overlay');
   const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
   
   navContainer.classList.toggle('active');
   overlay.classList.toggle('active');
   
   // Update menu icon
   const menuIcon = mobileMenuBtn.querySelector('i');
   if (navContainer.classList.contains('active')) {
       menuIcon.classList.remove('fa-bars');
       menuIcon.classList.add('fa-times');
   } else {
       menuIcon.classList.remove('fa-times');
       menuIcon.classList.add('fa-bars');
   }
}

// close mobile menu when clicking outside
document.addEventListener('click', (e) => {
   const navContainer = document.querySelector('.nav-container');
   const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
   
   if (navContainer.classList.contains('active') && 
       !navContainer.contains(e.target) && 
       !mobileMenuBtn.contains(e.target)) {
       toggleMobileMenu();
   }
});

// prevent menu from staying open on window resize
window.addEventListener('resize', () => {
   if (window.innerWidth > 1024) {
       const navContainer = document.querySelector('.nav-container');
       const overlay = document.querySelector('.mobile-menu-overlay');
       const menuIcon = document.querySelector('.mobile-menu-btn i');
       
       navContainer.classList.remove('active');
       overlay.classList.remove('active');
       menuIcon.classList.remove('fa-times');
       menuIcon.classList.add('fa-bars');
   }
});
/* modal */
function openBookingModal(workshop_id) {
    const modal = document.getElementById('bookingModal');
    const workshopId = document.getElementById('workshopId');
    modal.classList.add('active');
    workshopId.value = workshop_id;
    document.body.style.overflow = 'hidden';
}

function closeBookingModal() {
    const modal = document.getElementById('bookingModal');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

function validateSeats(input) {
    const value = parseInt(input.value);
    if (value < 1) {
        input.value = 1;
    } else if (value > 10) {
        input.value = 10;
    }
}

// handle booking form submission
document.getElementById('bookingForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const submitButton = this.querySelector('.submit-btn');
    submitButton.disabled = true;
    submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';

    try {
        const formData = new FormData(this);
        const csrfToken = formData.get('csrfmiddlewaretoken');
        const bookingData = {
            workshopId: formData.get('workshop_id'),
            seats: parseInt(formData.get('seats'))
        };

        const response = await fetch(this.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken, 
            },
            body: JSON.stringify(bookingData)
        });

        const result = await response.json();
        closeBookingModal();
        this.reset();
        window.location.reload();
    } catch (error) {
        console.error('Error booking seats:', error);
    } 
});

// close modal when clicking outside
document.getElementById('bookingModal').addEventListener('click', function(event) {
    if (event.target === this) {
        closeBookingModal();
    }
});

function validateRating(input) {
    const value = parseInt(input.value);
    if (value < 1) {
        input.value = 1;
    } else if (value > 5) {
        input.value = 5;
    }
}
// Rating Modal Functions
function openRatingModal(workshopId) {
    const modal = document.getElementById('ratingModal');
    const workshopIdInput = document.getElementById('workshopRatingId');
    modal.classList.add('active');
    workshopIdInput.value = workshopId;
    document.body.style.overflow = 'hidden';
}

function closeRatingModal() {
    const modal = document.getElementById('ratingModal');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Initialize rating stars functionality
document.addEventListener('DOMContentLoaded', function() {
    const ratingStars = document.querySelectorAll('.rating-stars i');
    const selectedRating = document.getElementById('selectedRating');

    ratingStars.forEach(star => {
        star.addEventListener('mouseover', function() {
            const rating = this.dataset.rating;
            updateStars(ratingStars, rating);
        });

        star.addEventListener('mouseleave', function() {
            const rating = selectedRating.value || 0;
            updateStars(ratingStars, rating);
        });

        star.addEventListener('click', function() {
            const rating = this.dataset.rating;
            selectedRating.value = rating;
            updateStars(ratingStars, rating);
        });
    });
});

function updateStars(stars, rating) {
    stars.forEach(star => {
        if (star.dataset.rating <= rating) {
            star.classList.remove('far');
            star.classList.add('fas');
        } else {
            star.classList.remove('fas');
            star.classList.add('far');
        }
    });
}

// Handle form submission
document.getElementById('ratingForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const submitButton = this.querySelector('.submit-btn');
    submitButton.disabled = true;
    submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...';

    try {
        const formData = new FormData(this);
        const csrfToken = formData.get('csrfmiddlewaretoken');
        const response = await fetch(this.action, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                workshop_id: formData.get('workshop_id'),
                rating: formData.get('rating'),
                feedback: formData.get('feedback')
            })
        });
    } catch (error) {
        console.error('Error submitting rating:', error);
    } finally {
        window.location.reload();
    }
});