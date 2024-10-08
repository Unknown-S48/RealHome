document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loginForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(this);

        fetch('/auth/login/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = data.redirect_url;
                } else {
                    messageDiv.textContent = data.message || 'An error occurred during login.';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                messageDiv.textContent = 'An error occurred. Please try again later.';
            });
    });
});