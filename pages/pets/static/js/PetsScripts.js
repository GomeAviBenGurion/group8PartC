document.addEventListener("DOMContentLoaded", async () => {
    console.log("DOM fully loaded and parsed");

    // Buttons and dropdowns
    const toggleButton = document.querySelector(".toggle-btn");
    const filterButtons = document.querySelectorAll(".filter-option"); // Select all filter buttons
    const applyFiltersButton = document.getElementById("applyFilters");

    const breedButton = document.getElementById("breedButton");
    const genderButton = document.getElementById("genderButton");
    const sizeButton = document.getElementById("sizeButton");
    const ageButton = document.getElementById("ageButton");

    const breedList = document.getElementById("breedList");
    const genderList = document.getElementById("genderList");
    const sizeList = document.getElementById("sizeList");
    const ageList = document.getElementById("ageList");

    let breeds = []; // Store breeds globally

    // Save original button text for resetting later
    breedButton.dataset.defaultText = breedButton.textContent;
    genderButton.dataset.defaultText = genderButton.textContent;
    sizeButton.dataset.defaultText = sizeButton.textContent;
    ageButton.dataset.defaultText = ageButton.textContent;

    // Toggle filter buttons visibility
    toggleButton.addEventListener("click", () => {
        filterButtons.forEach(button => button.classList.toggle("hidden"));
    });

    // Load breeds dynamically from available dogs
    try {
        const response = await fetch("/breeds");
        let rawBreeds = await response.json();
        console.log("Available breeds:", rawBreeds);

        if (!Array.isArray(rawBreeds)) {
            console.error("Error: Received invalid data from backend:", rawBreeds);
            return;
        }

        // Sort breeds alphabetically
        breeds = [...new Set(rawBreeds)].sort();
        console.log("Breeds after sorting:", breeds);

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

    function populateBreedDropdown() {
        breedList.innerHTML = "";

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
            breedButton.textContent = breedButton.dataset.defaultText;
            breedButton.classList.remove("selected");
            breedList.style.display = "none";
            searchInput.value = "";
            fetchFilteredDogs();
        });

        breedList.appendChild(clearOption);
        updateBreedList(breeds);
    }

    function updateBreedList(breedArray) {
        breedList.querySelectorAll(".dropdown-item").forEach(item => item.remove());

        breedArray.forEach(breed => {
            const li = document.createElement("li");
            li.textContent = breed;
            li.classList.add("dropdown-item");

            li.addEventListener("click", () => {
                breedButton.textContent = breed;
                breedButton.classList.add("selected");
                breedList.style.display = "none";
            });

            breedList.appendChild(li);
        });
    }

    function populateList(options, container, button) {
        container.innerHTML = "";

        const clearOption = document.createElement("li");
        clearOption.textContent = "Clear Selection";
        clearOption.classList.add("clear-option");
        clearOption.addEventListener("click", () => {
            button.textContent = button.dataset.defaultText;
            button.classList.remove("selected");
            container.style.display = "none";
            fetchFilteredDogs();
        });

        container.appendChild(clearOption);

        options.forEach(option => {
            const li = document.createElement("li");
            li.textContent = option;
            li.classList.add("dropdown-item");

            li.addEventListener("click", () => {
                button.textContent = option;
                button.classList.add("selected");
                container.style.display = "none";
            });

            container.appendChild(li);
        });
    }

    async function fetchFilteredDogs() {
        let queryParams = [];

        if (breedButton.textContent !== "Breed") {
            queryParams.push(`breed=${encodeURIComponent(breedButton.textContent)}`);
        }
        if (genderButton.textContent !== "Gender") {
            queryParams.push(`gender=${encodeURIComponent(genderButton.textContent.toLowerCase())}`);
        }
        if (sizeButton.textContent !== "Size") {
            queryParams.push(`size=${encodeURIComponent(sizeButton.textContent)}`);
        }
        if (ageButton.textContent !== "Age") {
            queryParams.push(`age=${encodeURIComponent(ageButton.textContent)}`);
        }

        let queryString = queryParams.length > 0 ? `?${queryParams.join("&")}` : "";

        try {
            let response = await fetch(`/pets${queryString}`);
            let htmlContent = await response.text();
            let parser = new DOMParser();
            let doc = parser.parseFromString(htmlContent, "text/html");
            let newDogsGrid = doc.querySelector(".dogs-grid");

            document.querySelector(".dogs-grid").innerHTML = newDogsGrid.innerHTML;
        } catch (error) {
            console.error("Error fetching filtered dogs:", error);
        }
    }

    applyFiltersButton.addEventListener("click", fetchFilteredDogs);

    function toggleDropdown(button, dropdown) {
        button.addEventListener("click", () => {
            dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
        });
    }

    [breedButton, genderButton, sizeButton, ageButton].forEach(button => {
        toggleDropdown(button, button.nextElementSibling);
    });

    document.addEventListener("click", event => {
        [breedButton, genderButton, sizeButton, ageButton].forEach(button => {
            const dropdown = button.nextElementSibling;
            if (!button.contains(event.target) && !dropdown.contains(event.target)) {
                dropdown.style.display = "none";
            }
        });
    });

    document.getElementById("clearAllFilters").addEventListener("click", () => {
        [breedButton, genderButton, sizeButton, ageButton].forEach(button => {
            button.textContent = button.dataset.defaultText;
            button.classList.remove("selected");
        });
        fetchFilteredDogs();
    });
});
