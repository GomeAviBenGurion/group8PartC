from flask import Blueprint, render_template, redirect, url_for, session

# homepage blueprint definition
pets = Blueprint(
    'pets',
    __name__,
    static_folder='static',
    static_url_path='/pets',
    template_folder='templates'
)

# Dog data
dogs = [
    {"dog_id": 1, "name": "Buddy", "gender": "male",
     "image": "https://image.petmd.com/files/styles/978x550/public/2024-06/hip-dysplasia-in-dogs.jpg?w=1080&q=75"},
    {"dog_id": 1, "name": "Bella", "gender": "female",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg?h=430&w=710&hash=7FEB820D235A44B76B271060E03572C7"},
    {"dog_id": 1, "name": "Max", "gender": "male",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/border-collie-tongue-out.jpg"},
    {"dog_id": 1, "name": "Lucy", "gender": "male",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/german-shepherd.jpg"},
    {"dog_id": 1, "name": "Charlie", "gender": "male",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/australian-cattle-dog-dandelions.jpg"},
    {"dog_id": 1, "name": "Daisy", "gender": "female",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/rottweiler-on-grass.jpg"},
    {"dog_id": 1, "name": "Buddy", "gender": "male",
     "image": "https://image.petmd.com/files/styles/978x550/public/2024-06/hip-dysplasia-in-dogs.jpg?w=1080&q=75"},
    {"dog_id": 1, "name": "Bella", "gender": "female",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg?h=430&w=710&hash=7FEB820D235A44B76B271060E03572C7"},
    {"dog_id": 1, "name": "Max", "gender": "male",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/border-collie-tongue-out.jpg"},
    {"dog_id": 1, "name": "Lucy", "gender": "male",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/german-shepherd.jpg"},
    {"dog_id": 1, "name": "Charlie", "gender": "male",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/australian-cattle-dog-dandelions.jpg"},
    {"dog_id": 1, "name": "Daisy", "gender": "female",
     "image": "https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/rottweiler-on-grass.jpg"}
]

# Gender icons
gender_icons = {
    "male": '<i class="fa fa-mars fa-lg" style="color: #2196F3;"></i>',
    "female": '<i class="fa fa-venus fa-lg" style="color: #E91E63;"></i>',
}


# Route
@pets.route("/pets")
def index():
    return render_template("pets.html", active_page="pets", dogs=dogs, gender_icons=gender_icons,is_logged_in=session.get('logged_in', False))
