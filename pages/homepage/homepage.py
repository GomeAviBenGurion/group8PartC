from flask import Blueprint, render_template, redirect, url_for, session, request, jsonify

# homepage blueprint definition
homepage = Blueprint(
    'homepage',
    __name__,
    static_folder='static',
    static_url_path='/homepage',
    template_folder='templates'
)


# Routes
@homepage.route('/')
def index():
    # Retrieve the logged_out flag from the query parameters
    logged_out = request.args.get('logged_out', False)
    # Pass the flag to the template
    return render_template(
        "homepage.html",
        active_page="homepage",
        is_logged_in=session.get('logged_in', False),
        logged_out=logged_out
    )


@homepage.route('/check-login', methods=['GET'])
def check_login():
    """Check if the user is logged in."""
    return jsonify({'logged_in': session.get('logged_in', False)})

