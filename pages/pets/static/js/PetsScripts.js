document.addEventListener("DOMContentLoaded", async () => {
    console.log("DOM fully loaded and parsed");

    // Buttons and dropdowns
    const toggleButton = document.querySelector(".toggle-btn");
    const filterButtonsGroup = document.querySelector(".filter-buttons-group");
    const filterButtons = document.querySelectorAll(".filter-option"); // Selects all filter buttons

    const breedButton = document.getElementById("breedButton");
    const breedList = document.getElementById("breedList");
    const breedItemsContainer = document.getElementById("breedItems");
    const breedSearch = document.getElementById("breedSearch");

    const genderButton = document.getElementById("genderButton");
    const genderList = document.getElementById("genderList");

    const sizeButton = document.getElementById("sizeButton");
    const sizeList = document.getElementById("sizeList");

    const ageButton = document.getElementById("ageButton");
    const ageList = document.getElementById("ageList");

    let breeds = []; // Store breeds globally

    // Save original button text for resetting later
    breedButton.dataset.defaultText = breedButton.textContent;
    genderButton.dataset.defaultText = genderButton.textContent;
    sizeButton.dataset.defaultText = sizeButton.textContent;
    ageButton.dataset.defaultText = ageButton.textContent;

    // Toggle filter buttons visibility
    toggleButton.addEventListener("click", () => {
        filterButtons.forEach(button => {
            button.classList.toggle("hidden");
        });
    });

    // Load breeds once on page load
    try {
        const response = await fetch("/breeds");
        let rawBreeds = await response.json();
        console.log("Breeds loaded (raw):", rawBreeds);

        if (!Array.isArray(rawBreeds)) {
            console.error("Error: Received invalid data from backend:", rawBreeds);
            return;
        }

        // Remove duplicates and sort alphabetically
        breeds = [...new Set(rawBreeds.map(breed => breed.trim()))].sort();
        console.log("Breeds after deduplication:", breeds);

        populateBreedDropdown(); // Call function to populate breed dropdown
    } catch (error) {
        console.error("Error fetching breeds:", error);
    }

    // Predefined filter data
    const genderOptions = ["Male", "Female"];
    const sizeOptions = ["Small", "Medium", "Large"];
    const ageOptions = ["Puppy", "2 to 7 years", "Adult"];

    // Populate other dropdowns (without search bar)
    populateList(genderOptions, genderList, genderButton);
    populateList(sizeOptions, sizeList, sizeButton);
    populateList(ageOptions, ageList, ageButton);

    // Function to populate Breed dropdown with search bar & clear option
    function populateBreedDropdown() {
        breedList.innerHTML = ""; // Clear existing dropdown

        // Create search bar
        const searchInput = document.createElement("input");
        searchInput.type = "text";
        searchInput.classList.add("search-bar");
        searchInput.placeholder = "Search breeds...";
        searchInput.addEventListener("input", () => {
            const searchText = searchInput.value.toLowerCase();
            const filteredBreeds = breeds.filter(breed => breed.toLowerCase().includes(searchText));
            updateBreedList(filteredBreeds);
        });

        breedList.appendChild(searchInput);

        // Add "Clear Selection" option
        const clearOption = document.createElement("li");
        clearOption.textContent = "Clear Selection";
        clearOption.classList.add("clear-option");
        clearOption.addEventListener("click", () => {
            breedButton.textContent = breedButton.dataset.defaultText; // Reset button text
            breedButton.classList.remove("selected"); // Remove selected style
            breedList.style.display = "none"; // Hide dropdown
            searchInput.value = ""; // Clear search
            updateBreedList(breeds); // Restore full list
        });

        breedList.appendChild(clearOption);

        // Populate breed list
        updateBreedList(breeds);
    }

    // Function to update the Breed list dynamically (Ensuring "Clear Selection" remains)
    function updateBreedList(breedArray) {
        // Remove previous items, keep "Clear Selection" and search bar
        breedList.querySelectorAll(".dropdown-item").forEach(item => item.remove());

        breedArray.forEach(breed => {
            const li = document.createElement("li");
            li.textContent = breed;
            li.classList.add("dropdown-item");

            li.addEventListener("click", () => {
                breedButton.textContent = breed; // Update button text
                breedButton.classList.add("selected"); // Change button color
                breedList.style.display = "none"; // Hide dropdown
            });

            breedList.appendChild(li);
        });
    }

    // Function to populate non-breed dropdowns
    function populateList(options, container, button) {
        container.innerHTML = ""; // Clear existing list

        // Add "Clear Selection" option
        const clearOption = document.createElement("li");
        clearOption.textContent = "Clear Selection";
        clearOption.classList.add("clear-option");
        clearOption.addEventListener("click", () => {
            button.textContent = button.dataset.defaultText; // Reset button text
            button.classList.remove("selected"); // Remove selected style
            container.style.display = "none"; // Hide dropdown
        });

        container.appendChild(clearOption);

        options.forEach(option => {
            const li = document.createElement("li");
            li.textContent = option;
            li.classList.add("dropdown-item");

            li.addEventListener("click", () => {
                button.textContent = option; // Update button text
                button.classList.add("selected"); // Change button color
                container.style.display = "none"; // Hide dropdown
            });

            container.appendChild(li);
        });
    }

    // Toggle dropdown visibility when clicking buttons
    function toggleDropdown(button, dropdown) {
        button.addEventListener("click", () => {
            dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
        });
    }

    toggleDropdown(breedButton, breedList);
    toggleDropdown(genderButton, genderList);
    toggleDropdown(sizeButton, sizeList);
    toggleDropdown(ageButton, ageList);

    // Close dropdowns when clicking outside
    document.addEventListener("click", (event) => {
        [breedButton, genderButton, sizeButton, ageButton].forEach(button => {
            const dropdown = button.nextElementSibling;
            if (!button.contains(event.target) && !dropdown.contains(event.target)) {
                dropdown.style.display = "none";
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", async () => {
    console.log("DOM fully loaded and parsed");

    // Buttons and dropdowns
    const toggleButton = document.querySelector(".toggle-btn");
    const filterButtons = document.querySelectorAll(".filter-option"); // Select all filter buttons
    const screenWidthThreshold = 768; // Adjust as needed

    let filtersHiddenByScreen = false; // Track whether filters were hidden by screen size

    // Function to check screen size and hide filters if needed
    function checkScreenSize() {
        if (window.innerWidth < screenWidthThreshold) {
            filterButtons.forEach(button => button.classList.add("hidden")); // Hide filters on small screens
            filtersHiddenByScreen = true; // Mark that they were hidden automatically
        } else {
            filterButtons.forEach(button => button.classList.remove("hidden")); // Show filters on larger screens
            filtersHiddenByScreen = false; // Reset the tracking variable
        }
    }

    // Toggle filters manually when clicking the toggle button
    toggleButton.addEventListener("click", () => {
        // Only allow toggling if the filters were NOT hidden due to screen size
        if (filtersHiddenByScreen && window.innerWidth < screenWidthThreshold) {
            filterButtons.forEach(button => button.classList.remove("hidden"));
            filtersHiddenByScreen = false;
        } else {
            filterButtons.forEach(button => button.classList.toggle("hidden"));
        }
    });

    // Run the screen size check on page load and when resizing
    checkScreenSize();
    window.addEventListener("resize", checkScreenSize);
});

