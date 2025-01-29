from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash

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

        # Backend validation (optional)
        if not name or not email or not password:
            return jsonify({"success": False, "message": "All fields are required."}), 400

        # TODO: Add logic to save user data to the database

        return jsonify({"success": True, "message": "Account created successfully!"}), 200


