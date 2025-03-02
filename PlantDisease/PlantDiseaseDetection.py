from PIL import Image
import numpy as np
import tensorflow as tf
from Gemini.GeminiGenAI import getExplanation

# Function to Load and Preprocess the Image using Pillow
def load_and_preprocess_image(image_path, target_size=(224, 224)):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.
    return img_array


# Function to Predict the Class of an Image
def predict_image_class(model, image_path, class_indices):
    preprocessed_img = load_and_preprocess_image(image_path)
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]

    explanation = None

    if predicted_class_name:
        gpt_query = f'what is {predicted_class_name}'
        explanation = getExplanation(gpt_query).replace("*", "")
    
    return predicted_class_name, explanation