from flask import Blueprint, render_template, session, jsonify, request, redirect, url_for
from db_connector import get_adoption_requests_by_user, cancel_adoption_request, delete_adoption_request

# my_requests blueprint definition
my_requests = Blueprint(
    'my_requests',
    __name__,
    static_folder='static',
    static_url_path='/my_requests',
    template_folder='templates'
)


# Route to render My Requests page
@my_requests.route('/my_requests')
def index():
    if 'user_email' not in session:
        return redirect(url_for('login.index'))

    user_email = session['user_email']
    adoption_requests = get_adoption_requests_by_user(user_email)

    return render_template("my_requests.html", is_logged_in=True, requests=adoption_requests)


# API Route to cancel a request (update status instead of deleting)
@my_requests.route('/cancel_request', methods=['POST'])
def cancel_request():
    request_id = request.json.get('request_id')

    if not request_id:
        return jsonify({"error": "Missing request_id"}), 400

    response, status_code = cancel_adoption_request(request_id)
    return jsonify(response), status_code


# API Route to delete a cancelled request
@my_requests.route('/delete_request', methods=['POST'])
def delete_request():
    request_id = request.json.get('request_id')

    if not request_id:
        return jsonify({"error": "Missing request_id"}), 400

    response, status_code = delete_adoption_request(request_id)
    return jsonify(response), status_code
