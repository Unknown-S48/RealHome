function checkAuthAndRedirect(isAuthenticated, loginUrl) {
    if (!isAuthenticated) {
        // Show alert
        Swal.fire({
            title: 'Sign In Required',
            text: 'Please sign in to list a property',
            icon: 'info',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sign In',
            cancelButtonText: 'Cancel'
        }).then((result) => {
            if (result.isConfirmed) {
                // Redirect to login page
                window.location.href = loginUrl;
            } else {
                // Redirect back to home page
                window.location.href = '/';
            }
        });
        return false;
    }
    return true;
}