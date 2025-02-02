document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search-by-photo-btn').onclick = function() {
        document.getElementById('uploadModal').style.display = 'flex';
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

            document.getElementById('fileName').innerText = file.name;
        }
    };

    document.getElementById('predict-btn').onclick = function() {
        const fileInput = document.getElementById('imageUpload');
        const file = fileInput.files[0];

        if (file) {
            const formData = new FormData();
            formData.append('file', file);

            fetch('/predict', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.breed) {
                    document.getElementById('breedResult').innerText = `Predicted Breed: ${data.breed}`;
                } else {
                    document.getElementById('breedResult').innerText = 'Could not identify the breed.';
                }
            })
            .catch(error => console.error('Error:', error));
        } else {
            alert('Please upload an image first.');
        }
    };
});
