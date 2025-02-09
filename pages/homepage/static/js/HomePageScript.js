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

            document.getElementById('uploadModal').style.display = 'flex';
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while checking login status.');
        }
    };

    // Alert when "Join Community" is clicked
    document.getElementById('join-community-btn').onclick = function() {
        alert('Oops! This feature isn\'t ready yet. We\'re still teaching our tech dogs how to build it. 🐶');
    };

    document.querySelector('.close-btn').onclick = function() {
        document.getElementById('uploadModal').style.display = 'none';
    };

    window.onclick = function(event) {
        const modal = document.getElementById('uploadModal');
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };

    document.getElementById('imageUpload').onchange = function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const uploadLabel = document.querySelector('.custom-file-upload');
                uploadLabel.style.backgroundImage = `url('${e.target.result}')`;
                uploadLabel.classList.add('uploaded');
                uploadLabel.querySelector('i').style.display = 'none';
            };
            reader.readAsDataURL(file);
        }
    };

    document.getElementById('predict-btn').onclick = async function() {
        const fileInput = document.getElementById('imageUpload');
        const file = fileInput.files[0];

        if (!file) {
            alert('Please upload an image first.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            let response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            let data = await response.json();

            if (response.ok) {
                document.getElementById('breedResult').innerText = `Predicted Breed: ${data.breed}`;
            } else {
                document.getElementById('breedResult').innerText = 'Could not identify the breed.';
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while processing your request.');
        }
    };
});
