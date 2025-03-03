import sys
sys.path.append('./CropRecommendation')
sys.path.append('./Gemini')
sys.path.append('./Database')

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import json
from PIL import Image

import numpy as np
import tensorflow as tf
from werkzeug.utils import secure_filename

from PlantDisease.PlantDiseaseDetection import predict_image_class

from CropRecommendation import getCropRecommendation
from Database.connectDB import DB
from Database.createTable import create_table
from Database.dbOperations import register_user, login_user, update_profile, get_user_profile

import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# middleware
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Load the pre-trained Crop Recomendation ML model and vectorizer
CropRecommendation_model = joblib.load(open(".\Models\CropRecommendation\model.joblib", 'rb'))
CropRecommendation_scaler = joblib.load(open(".\Models\CropRecommendation\scaler.joblib", 'rb'))

# Load the pre-trained ML model
PlantDisease_model = tf.keras.models.load_model(".\Models\PlantDisease\plant_disease_prediction_model.h5")
PlantDisease_class_indices = json.load(open(".\Models\PlantDisease\class_indices.json"))

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# connect database
db = DB("localhost", "SmartFarming", "postgres", "root")
connection = db.connect()
if connection != None:
    if create_table(connection):
        print("User Table Created")
    else:
        connection = None

@app.route('/api/check', methods=["GET"])
def check():
    return "API is working", 200

@app.route('/api/crop_recommendation', methods=['POST'])
def crop_recommendation():
    try:
        data = request.get_json()
        nitrogen = int(data['nitrogen'])
        phosphorus = int(data['phosphorus'])
        potassium = int(data['potassium'])
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        rainfall = float(data['rainfall'])
        ph = float(data['ph'])

        # print(nitrogen, phosphorus, potassium, temperature, humidity, rainfall, ph)

        if None in (nitrogen, phosphorus, potassium, temperature, humidity, rainfall, ph):
            return jsonify({"success":False,'message': 'Missing values'}), 200
        
        if temperature>100:
            return jsonify({"success":False, 'message': 'Temperature is very high'}), 200
        
        if temperature<0:
            return jsonify({"success":False, 'message': 'Temperature is too low'}), 200
        
        if ph>14 or ph<0:
            return jsonify({"success":False, 'message': 'Enter pH value between 0 and 14'}), 200

        predicted_crop, explanation = getCropRecommendation(CropRecommendation_model, CropRecommendation_scaler, nitrogen, phosphorus, potassium, temperature, humidity, rainfall, ph)

        return jsonify({"success":True, 'result': predicted_crop, 'explanation': explanation}), 200
    except Exception as e:
        return jsonify({"success":False, 'message': str(e)}), 400
    
def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/api/disease_detection', methods=['POST'])
def disease_detection():
    try:
        if 'file' not in request.files:
            return jsonify({"success": False, 'message': 'No file part in the request'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"success": False, 'message': 'No file selected for uploading'}), 400

        if file and allowed_file(file.filename):
            # Secure the filename to avoid any issues
            filename = secure_filename(file.filename)

            # Save the file temporarily
            temp_dir = os.path.join(os.getcwd(), 'tmp')
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)

            # Save the file to the temporary directory
            file_path = os.path.join(temp_dir, filename)
            file.save(file_path)

            prediction, explanation = predict_image_class(PlantDisease_model, file_path, PlantDisease_class_indices)

            os.remove(file_path)

            return jsonify({"success": True, 'result': prediction, 'explanation': explanation}), 200
        else:
            return jsonify({"success": False, 'message': 'Allowed file types are png, jpg, jpeg'}), 400
    except Exception as e:
        return jsonify({"success":False, 'message': str(e)}), 400

@app.route('/api/update_user', methods=['POST'])
def updateUser():
    try:
        data = request.get_json()
        email = str(data['email'])
        name = str(data['name'])
        gender = str(data['gender'])
        contact = str(data['phoneNo'])
        location = str(data['location'])
        dob = str(data['dob'])

        if None in (email, gender, contact, location, dob):
            return jsonify({"success":False, 'message': 'Missing values'}), 200
        
        user_creds = {
            'email': email,
            'name': name,
            'gender': gender,
            'contact': contact,
            'location': location,
            'dob': dob
        }
        # print(user_creds)

        # return jsonify({"success":True})

        response = update_profile(connection, user_creds)
        
        if response["success"]:
            return jsonify({"success":True, 'message': 'Profile updated successfully'}), 200
        else:
            return jsonify({"success":False, 'message': response['message']}), 200
        
    except Exception as e:
        return jsonify({"success":False, 'message': str(e)}), 400

@app.route('/api/register_user', methods=['POST'])
def registerUser():
    try:
        data = request.get_json()
        
        email = str(data['email'])
        password = str(data['password'])
        name = str(data['name'])
        
        if None in (email, password, name):
            return jsonify({"success":False, 'message': 'Missing values'}), 200
        
        if '@' not in email:
            return jsonify({"success":False, 'message': 'Invalid name or email'}), 200
        
        if len(password) < 8:
            return jsonify({"success":False, 'message': 'Password should be at least 8 characters'}), 200
        
        user = {
            'email': email,
            'password': password,
            'name': name
        }

        # print(type(connection))

        response = register_user(connection, user)

        if response["success"]:
            return jsonify({"success":True, 'message': 'User registered successfully. Login Again'}), 200
        else:
            return jsonify({"success":False, 'message': response['message']}), 200

    except Exception as e:
        return jsonify({"success":False, 'message': str(e)}), 400

@app.route('/api/login_user', methods=['POST'])
def loginUser():
    try:
        data = request.get_json()
        email = str(data['email'])
        password = str(data['password'])

        if None in (email, password):
            return jsonify({"success":False, 'message': 'Missing values'}), 200
        
        if '@' not in email:
            return jsonify({"success":False, 'message': 'Invalid username or email'}), 200
        
        user_creds = {
            'email': email,
            'password': password
        }

        response = login_user(connection, user_creds)

        if response['success']:
            token = response['token']
            return jsonify({"success":True, 'message': 'User logged in successfully', 'token': token}), 200
        else:
            return jsonify({"success":False, 'message': response['message']}), 200

    except Exception as e:
        return jsonify({"success":False, 'message': str(e)}), 400
    

@app.route('/api/get_user', methods=['POST'])
def getUser():
    try:
        data = request.get_json()
        token = str(data['token'])

        if token=="" or token==None:
            return jsonify({"success":False, 'message': 'Missing values'}), 200

        response = get_user_profile(connection, token)

        if response['success']:
            user = response['user']
            return jsonify({"success":True, 'message': 'User Details Fetched successfully', 'user': user}), 200
        else:
            return jsonify({"success":False, 'message': response['message']}), 200

    except Exception as e:
        return jsonify({"success":False, 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)