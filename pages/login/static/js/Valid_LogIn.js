document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");


    // Alert when "Google" is clicked
    document.getElementById('google-login-btn').onclick = function() {
        alert('Oops! This feature isn\'t ready yet. We\'re still teaching our tech dogs how to build it. 🐶');
    };

    // Alert when "Forgot Password" is clicked
    document.getElementById('forgot-password').onclick = function() {
        alert('Oops! This feature isn\'t ready yet. We\'re still teaching our tech dogs how to build it. 🐶');
    };

    function validateEmail(email) {
        return true
    }

    if (loginForm) {
        loginForm.addEventListener("submit", async function (event) {
            event.preventDefault(); // Prevent default form submission behavior

            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("logInPassword").value.trim();

            // Validate email and password
            if (validateEmail(email) && password) {
                try {
                    // Use fetch API for AJAX call
                    const response = await fetch('/login', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ email, password }),
                    });

                    const result = await response.json();

                    if (result.success) {
                        alert("Login successful!");

                        // Redirect to the homepage
                        window.location.href = "/";
                    } else {
                        alert(result.message || "Login failed! Please try again.");
                    }
                } catch (error) {
                    console.error("Error during login:", error);
                    alert("An error occurred. Please try again.");
                }
            } else if (!password) {
                alert("Password field is required!");
            }
        });
    } else {
        console.error("Login form not found!");
    }
});
