from bson import ObjectId
from flask import Blueprint, render_template, session, jsonify, request, redirect, url_for
from db_connector import requests_col  # Import database connection

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

    # Fetch requests from MongoDB
    adoption_requests = list(requests_col.find({"user_email": user_email}))

    # Convert `_id` to string & ensure `photo` exists
    for request in adoption_requests:
        request["_id"] = str(request["_id"])  # Convert ObjectId to string
        if "photo" not in request or not request["photo"]:
            request["photo"] = "https://cdn-icons-png.flaticon.com/512/4225/4225925.png"  # Default Image

    return render_template("my_requests.html", is_logged_in=True, requests=adoption_requests)


# API Route to cancel a request (update status instead of deleting)
@my_requests.route('/cancel_request', methods=['POST'])
def cancel_request():
    request_id = request.json.get('request_id')

    if not request_id:
        print("❌ Missing request_id in request")
        return jsonify({"error": "Missing request_id"}), 400

    try:
        object_id = ObjectId(request_id)  # Convert to ObjectId
        print(f"🔍 Request to cancel: {object_id}")  # Debugging line

        result = requests_col.update_one(
            {"_id": object_id},  # Query by ObjectId
            {"$set": {"status": "Cancelled"}}
        )

        if result.modified_count > 0:
            print(f"✅ Request {object_id} successfully cancelled.")
            return jsonify({"message": "Request status updated to Cancelled", "request_id": request_id})
        else:
            print(f"⚠️ Request {object_id} not found or already cancelled.")
            return jsonify({"error": "Request not found or already cancelled"}), 400
    except Exception as e:
        print(f"❌ Error in cancel_request: {e}")  # Debugging line
        return jsonify({"error": str(e)}), 400
