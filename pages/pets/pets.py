import sys
from datetime import datetime
from flask import Blueprint, render_template, session, jsonify, request
from db_connector import dogs_col

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
        breed_filter = request.args.get("breed")
        size_filter = request.args.get("size")
        gender_filter = request.args.get("gender")
        age_filter = request.args.get("age")

        # Construct MongoDB query
        query = {}

        if breed_filter:
            query["breed"] = breed_filter
        if size_filter:
            query["size"] = size_filter.lower()  # Ensure this matches the stored MongoDB field
        if gender_filter:
            query["sex"] = gender_filter.lower()  # Convert to lowercase for consistency

        # Fetch filtered dogs from MongoDB
        dogs = list(dogs_col.find(query))

        # Process each dog's data
        for dog in dogs:
            dog["_id"] = str(dog["_id"])  # Convert ObjectId to string

            # Ensure `photo` field exists
            if "photos" in dog and isinstance(dog["photos"], list) and len(dog["photos"]) > 0:
                dog["photo"] = dog["photos"][0]  # Take the first photo
            else:
                dog["photo"] = "https://cdn-icons-png.flaticon.com/512/4225/4225925.png"

            # Calculate and apply age category
            dog["age_category"] = get_age_category(dog.get("date_of_birth"))

        # Apply age filter after fetching data (since it's derived dynamically)
        if age_filter:
            dogs = [dog for dog in dogs if dog["age_category"] == age_filter]

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
        breeds = dogs_col.distinct("breed")  # Fetch unique breed values
        return jsonify(breeds)  # Return list of unique breeds
    except Exception as e:
        print("MongoDB Error:", e)  # Print error to Flask console
        return jsonify({"error": str(e)}), 500  # Return error to frontend
