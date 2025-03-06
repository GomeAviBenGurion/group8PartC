import os
from datetime import datetime
from bson import ObjectId
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load environment variables from .env file
load_dotenv()

# MongoDB Connection
uri = os.getenv("DB_URI")

# Create MongoDB Client
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['SophieBocaDB']

# Define collections
adopters_col = mydatabase['Adopters']
requests_col = mydatabase['AdoptionsRequests']
dogs_col = mydatabase['Dogs']
breeds_col = mydatabase['Breeds']


# Database functions
def find_adopter_by_email(email):
    """Find an adopter by email."""
    return adopters_col.find_one({"email": email})


def insert_adopter(name, email, hashed_password):
    """Insert a new adopter into the database."""
    user_data = {"name": name, "email": email, "password": hashed_password}
    adopters_col.insert_one(user_data)


def verify_adopter(email, password, check_password_hash):
    """Authenticate user by verifying the password."""
    user = find_adopter_by_email(email)
    if not user or not check_password_hash(user["password"], password):
        return None
    return user


def find_dogs(filters):
    """Fetch dogs from the database based on filters."""
    query = {}

    if filters.get("breed"):
        query["breed"] = filters["breed"]
    if filters.get("size"):
        query["size"] = filters["size"].lower()  # Ensure consistency in database
    if filters.get("gender"):
        query["sex"] = filters["gender"].lower()  # Convert to lowercase

    dogs = list(dogs_col.find(query))

    for dog in dogs:
        dog["_id"] = str(dog["_id"])  # Convert ObjectId to string

        # Ensure `photo` field exists
        if "photos" in dog and isinstance(dog["photos"], list) and len(dog["photos"]) > 0:
            dog["photo"] = dog["photos"][0]  # Take the first photo
        else:
            dog["photo"] = "https://cdn-icons-png.flaticon.com/512/4225/4225925.png"

    return dogs


def get_unique_breeds():
    """Fetch unique dog breeds from the database."""
    return dogs_col.distinct("breed")


def get_dog_by_id(dog_id):
    """Fetch a dog's details from the database."""
    try:
        dog = dogs_col.find_one({"_id": ObjectId(dog_id)})
        if not dog:
            return None

        # Convert ObjectId to string
        dog["_id"] = str(dog["_id"])

        # Ensure the `photos` field is available
        if "photos" not in dog or not isinstance(dog["photos"], list) or len(dog["photos"]) == 0:
            dog["photos"] = ["https://cdn-icons-png.flaticon.com/512/4225/4225925.png"]  # Default image

        return dog
    except Exception as e:
        print(f"Error fetching dog details: {e}")
        return None


def get_breed_details(breed):
    """Fetch breed details from the database."""
    return breeds_col.find_one({"breed": breed})


def submit_adoption_request(user_email, dog):
    """Submit an adoption request for a dog."""
    try:
        dog_id = str(dog["_id"])
        existing_request = requests_col.find_one({"user_email": user_email, "dog_id": dog_id})

        if existing_request:
            return {"error": "Heads up! 🐾 You've already submitted an adoption request for this pup. 🐶"}, 400

        # Extract dog's first photo
        photo_url = dog["photos"][0] if "photos" in dog and len(
            dog["photos"]) > 0 else "https://cdn-icons-png.flaticon.com/512/4225/4225925.png"

        # Prepare adoption request document
        adoption_request = {
            "user_email": user_email,
            "dog_id": dog_id,
            "dog_name": dog["name"],
            "photo": photo_url,
            "status": "Pending",
            "request_date": datetime.today().strftime("%Y-%m-%d")
        }

        # Insert into database
        requests_col.insert_one(adoption_request)
        return {"message": "Yay! 🎉 Your adoption request has been submitted successfully! 🐾"}, 200

    except Exception as e:
        print(f"Error processing adoption request: {e}")
        return {"error": "An error occurred while processing the adoption request"}, 500


def get_adoption_requests_by_user(user_email):
    """Fetch adoption requests for a specific user."""
    try:
        adoption_requests = list(requests_col.find({"user_email": user_email}))

        # Convert `_id` to string & ensure `photo` exists
        for request in adoption_requests:
            request["_id"] = str(request["_id"])
            if "photo" not in request or not request["photo"]:
                request["photo"] = "https://cdn-icons-png.flaticon.com/512/4225/4225925.png"  # Default Image

        return adoption_requests
    except Exception as e:
        print(f"Error fetching adoption requests: {e}")
        return []


def cancel_adoption_request(request_id):
    """Update request status to 'Cancelled'."""
    try:
        object_id = ObjectId(request_id)
        result = requests_col.update_one(
            {"_id": object_id},
            {"$set": {"status": "Cancelled"}}
        )

        if result.modified_count > 0:
            return {"message": "Request status updated to Cancelled", "request_id": request_id}, 200
        else:
            return {"error": "Request not found or already cancelled"}, 400
    except Exception as e:
        print(f"Error cancelling request: {e}")
        return {"error": str(e)}, 400


def delete_adoption_request(request_id):
    """Delete an adoption request if it's cancelled."""
    try:
        object_id = ObjectId(request_id)
        result = requests_col.delete_one({"_id": object_id, "status": "Cancelled"})

        if result.deleted_count > 0:
            return {"message": "Gone! 🐾 Your request has been deleted successfully. 🗑️", "request_id": request_id}, 200
        else:
            return {"error": "Request not found or not in 'Cancelled' status"}, 400
    except Exception as e:
        print(f"Error deleting request: {e}")
        return {"error": str(e)}, 400
