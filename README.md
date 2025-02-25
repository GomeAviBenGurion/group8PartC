# SophieBoca - Dog Adoption Website

## Part A

### Project Overview
SophieBoca is a user-friendly platform aimed at connecting people interested in adopting dogs with shelters, foster homes, and animal associations. Our mission is to make the adoption process accessible and efficient for both adopters and organizations, encouraging lasting bonds between dogs and their new families.

### Key Features
1. **User Accounts** - Separate registration for adopters and associations.
2. **Detailed Dog Profiles** - Information on breed, temperament, energy level, health status, and more.
3. **Advanced Search** - Filters by size, age, breed, energy level, and even a photo-based breed matching tool.
4. **Adoption Requests** - Users can submit adoption requests, view statuses, and track adoption history.

### Screenshots

| **Home Page** | **Dogs Page** |
| --- | --- |
| ![Home Page](static/media/screenshots/HomePage.png) | ![Dogs Page](static/media/screenshots/DogsPage.png) |

## Part B

### Main Flows on the Site

#### User Flows:

- **Adoption Request:** Users can browse available dogs on the Pets page. When they click the "Adopt" button on a dog's details page, a request is sent to the association. The user is notified with a popup message, confirming that the association will contact them via email.
- **Association Management:** Logged-in associations can manage pets and view adoption requests through dedicated pages.
- **Create Account and Login:** Separate signup pages for adopters and associations, with client-side form validation.

---

### Assumptions Regarding Use

- There is no user profile page to track requests, as an adopter is likely to adopt only one dog.
- Logging in opens all dog cards for the user. Currently, only the first row is enabled without login (to be fully implemented in Part 3).
- **Dynamic Content:** Many pages are implemented in JavaScript, preparing for future database integration for dynamic data (e.g., pets, adoption requests).
- **Feature Rollout:** Some features (e.g., filtering on the Pets page, user registration) are placeholders and will be implemented in later parts.
- **Association Access:** Association functionalities are accessed via a special button on the login page (no backend authentication yet).

---

### Repeating Elements

- **Header:** Navigation bar with a logo and links to core sections (Home, Pets, About, Contact).
- **Footer:** Includes copyright information, social media links, and consistent styling.
- **Popup Message:** Used for various actions, like adoption confirmation or feature placeholders.

---

### Responsive Design

The site is designed to be fully responsive, using:

- **CSS Media Queries:** Adapts layout for smaller screens (e.g., the navigation bar becomes a hamburger menu).

#### Example:

```css
@media (max-width: 1300px) {
    .nav-links {
        display: none;
        flex-direction: column;
    }

    .nav-links.show {
        display: flex;
    }

    .hamburger {
        display: flex;
    }
}
```
### CSS Animation 

```css
.primary-btn:hover {
    transform: scale(1.08);
    transition: transform 0.3s;
}
```
---

## Event Functions

### Examples:

1. **Hamburger Menu Toggle:**

   ```javascript
   document.querySelector('.hamburger').addEventListener('click', () => {
       document.querySelector('.nav-links').classList.toggle('show');
   });
   ```
2. **Adopt Button Popup:**
   ```javascript
    document.getElementById('adopt-btn').addEventListener('click', () => {
        document.getElementById('popup-message').style.display = 'block';
    });
   ```
---

## Forms and Validations

### Existing Forms:

- Create Account: Name, email, password, and confirm password validation.
- Sign Up Association: Additional fields for phone and address.
- Login Form: Email and password validation.

### Validation Examples

The forms on the site include several input validations to ensure data integrity and user experience:

- Create Account Form: Requires the user's name, email, password, and confirmation password. Fields must adhere to strict validation rules, such as email format and password strength.
- Sign Up Association Form: Includes fields for phone number and address, in addition to those in the Create Account Form, ensuring proper contact details.
- Login Form: Ensures email and password fields are correctly formatted and not empty. Password strength is not re-verified, as it was validated during registration.

These validations offer real-time feedback, guiding users to correct any mistakes or omissions during input.

 ---
 #   Part C
 
 
