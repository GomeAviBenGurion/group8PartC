from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for
from werkzeug.security import check_password_hash
from db_connector import verify_adopter  # Import authentication function

# Define the blueprint
login = Blueprint(
    'login',
    __name__,
    static_folder='static',
    static_url_path='/login/static',
    template_folder='templates'
)


# Routes
@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')  # Render the login page

    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "message": "No JSON data provided."}), 400

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"success": False, "message": "Email and password are required."}), 400

        # Authenticate user
        user = verify_adopter(email, password, check_password_hash)
        if not user:
            return jsonify({"success": False, "message": "Oops! ❌ Wrong email or password. Try again! 🔑"}), 401

        # Store user session
        session['logged_in'] = True
        session['user_id'] = str(user["_id"])  # Store user ID in session
        session['user_name'] = user["name"]
        session['user_email'] = user["email"]

        return jsonify({"success": True, "message": "You're in! 🎉 Welcome back to the pack! 🦴"}), 200


@login.route('/logout', methods=['GET'])
def logout():
    session.clear()  # Clear session data
    return redirect(url_for('homepage.index', logged_out=True))
