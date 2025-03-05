document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");

    // Alert when "Google" is clicked
    document.getElementById('google-login-btn').onclick = function() {
        alert('Oops! This feature isn\'t ready yet. We\'re still teaching our tech dogs how to build it. 🐶');
    };

    // Check if email is entered before "Forgot Password" alert
    document.getElementById('forgot-password').onclick = function() {
        const email = document.getElementById("email").value.trim();

        if (!email) {
            alert('Please enter your email before resetting your password. 📧');
            return;
        }

        alert('No worries! 📧 A password reset email is on its way. Check your inbox! 🐾');
    };

    if (loginForm) {
        loginForm.addEventListener("submit", async function (event) {
            event.preventDefault(); // Prevent default form submission behavior

            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("logInPassword").value.trim();

            if (email && password) {
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
                        alert("You're in! 🎉 Welcome back to the pack! 🦴");

                        // Redirect to the homepage
                        window.location.href = "/";
                    } else {
                        alert(result.message || "Login failed! Please try again.");
                    }
                } catch (error) {
                    console.error("Error during login:", error);
                    alert("An error occurred. Please try again.");
                }
            } else {
                alert("Both email and password are required!");
            }
        });
    } else {
        console.error("Login form not found!");
    }
});