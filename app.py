import sys
sys.path.append('./CropRecommendation')
sys.path.append('./Gemini')

from flask import Flask, request, jsonify
from flask_cors import CORS
from CropRecommendation import getCropRecommendation

app = Flask(__name__)

CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5173"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})


@app.route('/api/crop_recommendation', methods=['POST'])
def crop_recommendation():
    try:
        print(request)
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

        predicted_crop, explanation = getCropRecommendation(nitrogen, phosphorus, potassium, temperature, humidity, rainfall, ph)

        return jsonify({"success":True, 'result': predicted_crop, 'explanation': explanation}), 200
    except Exception as e:
        return jsonify({"success":False, 'message': str(e)}), 400
    
@app.route('/api/disease_detection', methods=['POST'])
def disease_detection():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=8080)