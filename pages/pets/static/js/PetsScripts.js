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

    // Function to toggle the visibility of the "Search by photo" text based on screen width
    function toggleSearchText() {
        const searchText = document.querySelector(".search-by-photo-btn .search-text");
        if (searchText) {
            if (window.innerWidth <= 705) {
                searchText.classList.add("hidden");
            } else {
                searchText.classList.remove("hidden");
            }
        } else {
            console.log("Search text element not found.");
        }
    }

    // Run the toggleSearchText function on page load and when resizing the window
    toggleSearchText();
    window.addEventListener('resize', toggleSearchText);
});
