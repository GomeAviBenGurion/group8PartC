from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for, flash

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
        try:
            # Try to parse JSON from the request
            data = request.get_json()
            if not data:
                return jsonify({"success": False, "message": "No JSON data provided."}), 400

            email = data.get('email')
            password = data.get('password')

            # Dummy login logic for testing
            if email == "gomeavigdor@gmail.com" and password == "1":
                session['logged_in'] = True
                return jsonify({"success": True, "message": "Login successful!"})
            else:
                return jsonify({"success": False, "message": "Invalid credentials."}), 401
        except Exception as e:
            return jsonify({"success": False, "message": f"Error processing request: {str(e)}"}), 500


@login.route('/logout', methods=['GET'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('homepage.index', logged_out=True))


