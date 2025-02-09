from flask import Blueprint, render_template, redirect, url_for, session, request, jsonify
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
import numpy as np
import json
import urllib.request
import io

# homepage blueprint definition
homepage = Blueprint(
    'homepage',
    __name__,
    static_folder='static',
    static_url_path='/homepage',
    template_folder='templates'
)

# Load ImageNet class index
url = "https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json"
with urllib.request.urlopen(url) as response:
    imagenet_classes = json.load(response)

# Load the pre-trained EfficientNet model from TensorFlow Hub
model_url = "https://tfhub.dev/google/efficientnet/b0/classification/1"
model = hub.KerasLayer(model_url, input_shape=(224, 224, 3))

def load_and_preprocess_image(image):
    """Load and preprocess the image for prediction."""
    img = Image.open(image).convert("RGB")
    img = img.resize((224, 224))  # EfficientNet input size
    img_array = np.array(img) / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def predict_breed(image):
    """Predict the primary dog breed from the image."""
    img_array = load_and_preprocess_image(image)
    predictions = model(img_array).numpy().flatten()

    # Filter for dog breed classes (ImageNet classes 151-268)
    dog_breed_indices = np.argmax(predictions)
    dog_predictions = str(dog_breed_indices)

    # Get the class with the highest confidence score within dog breeds
    if dog_predictions:
        original_breed = imagenet_classes[dog_predictions][1]
        return original_breed
    else:
        return "Unknown Breed"


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


@homepage.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        breed = predict_breed(file)
        return jsonify({'breed': breed})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@homepage.route('/check-login', methods=['GET'])
def check_login():
    """Check if the user is logged in."""
    return jsonify({'logged_in': session.get('logged_in', False)})

