from flask import Blueprint, render_template, session, jsonify, request

# my_requests blueprint definition
my_requests = Blueprint(
    'my_requests',
    __name__,
    static_folder='static',
    static_url_path='/my_requests',
    template_folder='templates'
)

# Sample demo data (Replace this with actual database queries)
sample_requests = [
    {"id": 1, "dog_name": "Buddy", "status": "Pending", "request_date": "2024-03-01", "image": ""},
    {"id": 2, "dog_name": "Bella", "status": "Approved", "request_date": "2024-02-20", "image": ""},
    {"id": 3, "dog_name": "Charlie", "status": "Rejected", "request_date": "2024-02-15", "image": ""}
]

# Route to render My Requests page
@my_requests.route('/my_requests')
def index():
    is_logged_in = session.get('logged_in', False)

    return render_template("my_requests.html", is_logged_in=is_logged_in, requests=sample_requests)

# API Route to cancel a request (update status instead of deleting)
@my_requests.route('/cancel_request', methods=['POST'])
def cancel_request():
    request_id = request.json.get('request_id')

    # Simulate status update (Replace this with actual DB update)
    for req in sample_requests:
        if req['id'] == request_id:
            req['status'] = "Cancelled"

    return jsonify({"message": "Request status updated to Cancelled", "request_id": request_id})
