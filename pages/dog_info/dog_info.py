from flask import Blueprint, render_template, session, jsonify
from db_connector import get_dog_by_id, get_breed_details, submit_adoption_request
from datetime import datetime

# Define blueprint
dog_info = Blueprint(
    'dog_info',
    __name__,
    static_folder='static',
    static_url_path='/dog_info',
    template_folder='templates'
)


# Function to calculate age in years
def calculate_age(date_of_birth):
    """Calculate a dog's age in years and months."""
    if not date_of_birth:
        return "Unknown"

    try:
        birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
        today = datetime.today()

        # Calculate full years
        years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # Calculate months (remainder after years)
        months = (today.month - birth_date.month) % 12
        if today.day < birth_date.day:
            months -= 1  # Adjust if the day hasn't passed yet

        # Ensure months are within a valid range
        if months < 0:
            months += 12
            years -= 1

        # Convert to float format (e.g., 1.4 years for 1 year, 4 months)
        age = round(years + months / 12, 1)
        return f"{age} years"

    except Exception as e:
        print(f"Error calculating age: {e}")
        return "Unknown"


# Route to fetch and display dog details
@dog_info.route('/dog_info/<dog_id>')
def index(dog_id):
    try:
        # Fetch the dog's details
        dog = get_dog_by_id(dog_id)

        if not dog:
            return "Dog not found", 404

        # Fetch breed details
        breed_details = get_breed_details(dog["breed"])

        # Calculate and include age in years
        dog["age"] = calculate_age(dog.get("date_of_birth"))

        # Ensure association info exists
        association_info = dog.get("non_profit", {"name": "Unknown", "address": "No address available"})

        return render_template(
            "dog_info.html",
            dog=dog,
            breed_details=breed_details,
            association_info=association_info,
            is_logged_in=session.get('logged_in', False)
        )

    except Exception as e:
        print(f"Error fetching dog details: {e}")
        return "An error occurred", 500


# Route to handle adoption requests
@dog_info.route('/adopt/<dog_id>', methods=['POST'])
def adopt_dog(dog_id):
    if 'user_email' not in session:
        return jsonify({"error": "User not logged in"}), 401  # Unauthorized

    try:
        # Fetch the dog's details
        dog = get_dog_by_id(dog_id)

        if not dog:
            return jsonify({"error": "Dog not found"}), 404  # Not found

        # Submit adoption request
        response, status_code = submit_adoption_request(session['user_email'], dog)
        return jsonify(response), status_code

    except Exception as e:
        print(f"Error processing adoption request: {e}")
        return jsonify({"error": "An error occurred while processing the adoption request"}), 500
