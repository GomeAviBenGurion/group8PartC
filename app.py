from flask import Flask, session, redirect, url_for
from pages.homepage.homepage import homepage
from pages.pets.pets import pets
from pages.login.login import login
from pages.sign_up.sign_up import sign_up
from pages.dog_info.dog_info import dog_info


app = Flask(__name__)
app.secret_key = "Gome"

# Register blueprints
app.register_blueprint(homepage)
app.register_blueprint(pets)
app.register_blueprint(login)
app.register_blueprint(sign_up)
app.register_blueprint(dog_info)


if __name__ == '__main__':
    app.run(debug=True)
