document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registerForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(this);

        fetch('/auth/register/', {  // Make sure this URL matches your Django URL configuration
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
                'X-Requested-With': 'XMLHttpRequest'
            },
            credentials: 'same-origin'
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url;
                } else {
                    messageDiv.textContent = data.message || 'An error occurred during registration.';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                messageDiv.textContent = 'An error occurred. Please try again later.';
            });
    });
});