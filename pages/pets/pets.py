import sys
from datetime import datetime
from flask import Blueprint, render_template, session, jsonify, request
from db_connector import find_dogs, get_unique_breeds  # Import functions

# Force UTF-8 encoding to handle special characters
sys.stdout.reconfigure(encoding='utf-8')

# Define blueprint
pets = Blueprint(
    'pets',
    __name__,
    static_folder='static',
    static_url_path='/pets',
    template_folder='templates'
)

# Define Gender Icons
gender_icons = {
    "male": '<i class="fa fa-mars fa-lg" style="color: #2196F3;"></i>',
    "female": '<i class="fa fa-venus fa-lg" style="color: #E91E63;"></i>',
}


# Function to calculate age category
def get_age_category(dob):
    """Calculate age category based on date of birth."""
    if not dob:
        return "Unknown"

    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    age = (datetime.today() - birth_date).days // 365  # Convert days to years

    if age < 2:
        return "Puppy"
    elif 2 <= age <= 7:
        return "2 to 7 years"
    else:
        return "Adult"


# Route to fetch and filter dogs
@pets.route("/pets", methods=["GET"])
def index():
    try:
        # Retrieve filter values from request arguments
        filters = {
            "breed": request.args.get("breed"),
            "size": request.args.get("size"),
            "gender": request.args.get("gender"),
            "age": request.args.get("age"),
        }

        # Fetch filtered dogs from MongoDB
        dogs = find_dogs(filters)

        # Calculate age category for each dog
        for dog in dogs:
            dog["age_category"] = get_age_category(dog.get("date_of_birth"))

        # Apply age filter after fetching data (since it's derived dynamically)
        if filters["age"]:
            dogs = [dog for dog in dogs if dog["age_category"] == filters["age"]]

        print("Filtered Dogs:", dogs)  # Debugging output

        return render_template("pets.html", active_page="pets", dogs=dogs, gender_icons=gender_icons,
                               is_logged_in=session.get('logged_in', False))

    except Exception as e:
        print(f"Error fetching dogs: {e}")
        return render_template("pets.html", active_page="pets", dogs=[], gender_icons=gender_icons,
                               is_logged_in=session.get('logged_in', False))


@pets.route("/breeds")
def get_breeds():
    try:
        # Fetch unique breeds from existing dogs
        breeds = get_unique_breeds()
        return jsonify(breeds)  # Return list of unique breeds
    except Exception as e:
        print("MongoDB Error:", e)  # Print error to Flask console
        return jsonify({"error": str(e)}), 500  # Return error to frontend
