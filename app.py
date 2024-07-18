import os
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import model_from_json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the FaceNet model
json_file = open('keras-facenet-h5/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights('keras-facenet-h5/model.h5')
FRmodel = model

# Initialize a database (in-memory dictionary for demonstration)
database = {}

def img_to_encoding(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
    img = np.around(np.array(img) / 255.0, decimals=12)
    x_train = np.expand_dims(img, axis=0)
    embedding = model.predict_on_batch(x_train)
    return embedding / np.linalg.norm(embedding, ord=2)

@app.route('/signup', methods=['POST'])
def signup():
    if 'username' not in request.form or 'image' not in request.files:
        return jsonify({'error': 'Username and Image file required'}), 400

    username = request.form['username']
    image_file = request.files['image']

    # Save image to a temporary location
    image_path = f"temp/{username}.jpg"
    image_file.save(image_path)

    # Generate encoding and store in database
    encoding = img_to_encoding(image_path, FRmodel)
    database[username] = encoding.flatten().tolist()

    os.remove(image_path)  # Remove the temporary image file

    return jsonify({'message': 'Signup successful'}), 200

@app.route('/verify', methods=['POST'])
def verify():
    if 'image' not in request.files:
        return jsonify({'error': 'Image file required'}), 400

    image_file = request.files['image']

    # Save image to a temporary location
    image_path = "temp/verify.jpg"
    image_file.save(image_path)

    # Perform face recognition
    min_dist = 100
    identity = None
    encoding = img_to_encoding(image_path, FRmodel)

    for name, db_encoding in database.items():
        dist = np.linalg.norm(np.array(db_encoding) - encoding)
        if dist < min_dist:
            min_dist = dist
            identity = name

    os.remove(image_path)  # Remove the temporary image file

    if min_dist > 0.7 or identity is None:
        return jsonify({'message': 'Not recognized'}), 200
    else:
        return jsonify({'username': identity}), 200

if __name__ == '__main__':
    app.run(debug=True)
