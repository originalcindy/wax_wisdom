function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    const menuToggle = document.querySelector('.menu-toggle');
    
    sidebar.classList.toggle('active');
    
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

/* modal */
function openBookingModal(booking_id) {
    const modal = document.getElementById('bookingModal');
    const bookingId = document.getElementById('bookingId');
    modal.classList.add('active');
    bookingId.value = booking_id;
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
            bookingId: formData.get('bookingId'),
            seats: parseInt(formData.get('seats')),
            status: formData.get("status"),
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