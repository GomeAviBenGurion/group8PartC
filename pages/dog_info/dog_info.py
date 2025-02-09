from flask import Blueprint, render_template, session

# dog_info blueprint definition
dog_info = Blueprint(
    'dog_info',
    __name__,
    static_folder='static',
    static_url_path='/dog_info',
    template_folder='templates'
)

dogs = [
    {"dog_id": 1, "name": "Buddy", "gender": "male", "breed": "Labrador Retriever", "size": "Large", "age": "3 years",
     "energy_level": "High", "trainability": "Excellent", "sterilized": "Yes", "temperament": "Friendly, Outgoing",
     "shedding_category": "Moderate", "trainability_category": "High", "grooming_category": "Moderate",
     "association_name": "Happy Paws Rescue", "association_address": "123 Dog Street, Pet City",
     "breed_description": "Labrador Retrievers are friendly, outgoing, and high-spirited companions who have more than enough affection to go around for a family looking for a medium-to-large dog.",
     "photos": [
         "https://www.bellaandduke.com/wp-content/uploads/2024/10/A-guide-to-German-Shepherds-characteristics-personality-lifespan-and-more-featured-image-1024x683.webp",
         "https://worldanimalfoundation.org/wp-content/uploads/2024/02/german-shepherd-2-3.jpg",
         "https://www.vidavetcare.com/wp-content/uploads/sites/234/2022/04/german-shepherd-dog-breed-info.jpeg"]
     }
]


# Route to render dog info page
@dog_info.route('/dog_info')
def index():
    is_logged_in = session.get('logged_in', False)  # Defaults to False if not logged in
    return render_template("dog_info.html", dog=dogs[0], is_logged_in=is_logged_in)


