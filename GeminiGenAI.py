from dotenv import load_dotenv
import os
from google import genai


# load the env variables
load_dotenv()
api_key=os.getenv('API_KEY')


def getExplanation(query):
    res_text = None
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(model="gemini-2.0-flash", contents=query)
        res_text = response.text
    except Exception as e:
        res_text = str(e)
    return res_text