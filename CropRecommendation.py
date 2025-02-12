from GeminiGenAI import getExplanation
from CropData import getCropsData
import pandas as pd
import joblib

import warnings
warnings.filterwarnings('ignore')

# Load the pre-trained ML model and vectorizer
model = joblib.load(open(".\Models\CropRecommendation\model.joblib", 'rb'))
scaler = joblib.load(open(".\Models\CropRecommendation\scaler.joblib", 'rb'))


def getCropRecommendation(nitrogen, phosphorus, potassium, temperature, humidity, rainfall, ph):
    df = pd.DataFrame({
            'N': [nitrogen],
            'P': [phosphorus],
            'K': [potassium],
            'temperature': [temperature],
            'humidity': [humidity],
            'ph': [ph],
            'rainfall': [rainfall]
        })

    prediction_result = model.predict(scaler.transform(df))[0]
    predicted_crop = getCropsData()[prediction_result]

    explanation = None

    if predicted_crop:
        gpt_query = f'summaize the requirements for growing {predicted_crop} in 5 lines'
        explanation = getExplanation(gpt_query)

    return predicted_crop, explanation