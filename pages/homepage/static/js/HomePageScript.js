document.addEventListener('DOMContentLoaded', function() {
    // Check login status before opening the upload modal
    document.getElementById('search-by-photo-btn').onclick = async function() {
        try {
            let response = await fetch('/check-login');
            let data = await response.json();

            if (!data.logged_in) {
                alert('You must be logged in to use this feature.');
                window.location.href = '/login';
                return;
            }

            alert('Oops! This feature isn\'t ready yet. We\'re still teaching our tech dogs how to build it. 🐶');
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while checking login status.');
        }
    };

    // Alert when "Join Community" is clicked
    document.getElementById('join-community-btn').onclick = function() {
        alert('Oops! This feature isn\'t ready yet. We\'re still teaching our tech dogs how to build it. 🐶');
    };

});
