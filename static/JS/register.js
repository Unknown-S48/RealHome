document.addEventListener('DOMContentLoaded', function () {
    // Show/hide realtor fields
    const userTypeSelect = document.getElementById('userType');
    const realtorFields = document.getElementById('realtorFields');

    userTypeSelect.addEventListener('change', function () {
        realtorFields.style.display = this.value === 'realtor' ? 'block' : 'none';
    });

    // Form submission
    const registerForm = document.getElementById('registerForm');
    const messageDiv = document.getElementById('message');

    registerForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        messageDiv.innerHTML = ''; // Clear previous messages

        const url = this.action || window.location.href;

        try {
            const formData = new FormData(this);
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                },
                credentials: 'same-origin' // Include cookies
            });

            // Parse the JSON response
            const data = await response.json();

            // Check if the response was successful
            if (!response.ok) {
                throw new Error(data.message || 'Registration failed');
            }

            // Handle successful registration
            if (data.success) {
                messageDiv.innerHTML = '<div class="success-message">Registration successful! Redirecting...</div>';
                window.location.href = data.redirect_url;
            } else {
                messageDiv.innerHTML = `<div class="error-message">${data.message}</div>`;
            }

        } catch (error) {
            console.error('Registration error:', error);
            messageDiv.innerHTML = `<div class="error-message">${error.message || 'An error occurred during registration. Please try again.'}</div>`;
        }
    });
});