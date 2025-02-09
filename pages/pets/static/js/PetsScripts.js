console.log("PetsPageScript.js loaded");

// Toggle Filter Options
document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.querySelector('.toggle-btn');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            const filterOptions = document.querySelectorAll('.filter-option');
            filterOptions.forEach(option => {
                option.classList.toggle('hidden');
            });
        });
    }

});
