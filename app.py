from flask import Flask, session
from pages.homepage.homepage import homepage
from pages.pets.pets import pets
from pages.login.login import login
from pages.sign_up.sign_up import sign_up
from pages.dog_info.dog_info import dog_info
from pages.my_requests.my_requests import my_requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()  # Load environment variables from .env file

app.secret_key = os.getenv("SECRET_KEY")  # Use the secret key from .env

# Register blueprints
app.register_blueprint(homepage)
app.register_blueprint(pets)
app.register_blueprint(login)
app.register_blueprint(sign_up)
app.register_blueprint(dog_info)
app.register_blueprint(my_requests)


if __name__ == '__main__':
    app.run(debug=True)
