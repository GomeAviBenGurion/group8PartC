import sys

from flask import Blueprint, render_template, session, jsonify
from db_connector import dogs_col, breeds_col

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


# Route to display pets
@pets.route("/pets")
def index():
    try:
        # Fetch dogs from MongoDB
        dogs = list(dogs_col.find({}))
        for dog in dogs:
            dog["_id"] = str(dog["_id"])  # Convert ObjectId to string

            # Ensure the `photos` field exists and take the first image
            if "photos" in dog and isinstance(dog["photos"], list) and len(dog["photos"]) > 0:
                dog["photo"] = dog["photos"][0]  # Take the first photo
            else:
                dog["photo"] = "https://cdn-icons-png.flaticon.com/512/4225/4225925.png"  # Default image

        # Debugging: Print dog data to check `photo`
        print("Fetched Dogs:", dogs)

        return render_template("pets.html", active_page="pets", dogs=dogs, gender_icons=gender_icons,
                               is_logged_in=session.get('logged_in', False))

    except Exception as e:
        print(f"Error fetching dogs: {e}")  # Debugging
        return render_template("pets.html", active_page="pets", dogs=[], gender_icons=gender_icons,
                               is_logged_in=session.get('logged_in', False))


@pets.route("/breeds")
def get_breeds():
    try:
        breeds = list(breeds_col.find({}, {"breed": 1, "_id": 0}))  # Fetch breed names
        breed_list = [str(breed["breed"]) for breed in breeds]  # Ensure all values are strings
        return jsonify(breed_list)  # Return list of breeds
    except Exception as e:
        print("MongoDB Error:", e)  # Print error to Flask console
        return jsonify({"error": str(e)}), 500  # Return error to frontend


