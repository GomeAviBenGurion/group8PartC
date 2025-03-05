from flask import Blueprint, render_template, request, jsonify
from werkzeug.security import generate_password_hash
from db_connector import adopters_col  # Import from db_connector.py

# Define the blueprint
sign_up = Blueprint(
    'sign_up',
    __name__,
    static_folder='static',
    static_url_path='/sign_up/static',
    template_folder='templates'
)

# Routes
@sign_up.route('/sign_up', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('sign_up.html')

    elif request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # Backend validation
        if not name or not email or not password:
            return jsonify({"success": False, "message": "Woof! 🐾 Please fill in all the fields to continue."}), 400

        # Check if email already exists
        existing_user = adopters_col.find_one({"email": email})
        if existing_user:
            return jsonify({"success": False, "message": "Oops! ✉️ This email is already registered. Try another one!."}), 400

        # Hash password before storing
        hashed_password = generate_password_hash(password)

        # Save user to database
        user_data = {"name": name, "email": email, "password": hashed_password}
        adopters_col.insert_one(user_data)

        return jsonify({"success": True, "message": "Pawsome! 🐶 Your account has been created successfully! Time to unleash the fun"}), 200
