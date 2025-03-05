// Name Validation Function
function validateName(name) {
    const nameRegex = /^[A-Za-z]+(\s[A-Za-z]+)*$/; // Only letters and single spaces between words

    if (!name) {
        alert("Name field is required!");
        return false;
    }
    if (!nameRegex.test(name)) {
        alert("Name must only contain letters and single spaces between words!");
        return false;
    }
    return true;
}

// Email Validation Function
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Validates a proper email format

    if (!email) {
        alert("Email field is required!");
        return false;
    }
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address!");
        return false;
    }
    return true;
}

// Password Validation Function
function validatePassword(password) {
    const passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{6,}$/; // At least 1 uppercase, 1 lowercase, 1 number, 6+ chars

    if (!password) {
        alert("Password field is required!");
        return false;
    }
    if (!passwordRegex.test(password)) {
        alert(
            "Password must contain at least one uppercase letter, one lowercase letter, one number, and be at least 6 characters long!"
        );
        return false;
    }
    return true;
}

// Confirm Password Validation Function
function validateConfirmPassword(password, confirmPassword) {
    if (!confirmPassword) {
        alert("Confirm Password field is required!");
        return false;
    }
    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return false;
    }
    return true;
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("createAccountForm");
    if (form) {
        console.log("Form found. Adding event listener."); // Debugging log
        form.addEventListener("submit", async function (event) {
            event.preventDefault();

            const name = document.getElementById("createName").value.trim();
            const email = document.getElementById("createEmail").value.trim();
            const password = document.getElementById("createPassword").value.trim();
            const confirmPassword = document.getElementById("createConfirmPassword").value.trim();

            if (!validateName(name)) return;
            if (!validateEmail(email)) return;
            if (!validatePassword(password)) return;
            if (!validateConfirmPassword(password, confirmPassword)) return;

            // Server request
            try {
                const response = await fetch('/sign_up', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ name, email, password }),
                });

                const result = await response.json();
                if (result.success) {
                    alert(result.message || "Pawsome! 🐶 Your account has been created successfully! Time to unleash the fun!");
                    window.location.href = "/login"; // Redirect to the login page
                } else {
                    alert(result.message || "An error occurred. Please try again.");
                }
            } catch (error) {
                console.error("Error:", error);
                alert("An unexpected error occurred. Please try again.");
            }
        });
    } else {
        console.error("Form not found!"); // Debugging log
    }
});

