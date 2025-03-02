Project Overview
===============

This project aims to develop a smart farming backend using Python, focusing on creating a scalable and efficient system for multiple useful operatins. It is designed to be used in conjunction with a frontend application, which will handle user interactions and display data to the user. The project provides API endpoints for different smart farming operations.

Table of Contents
-----------------
* [Technology Required](#technology-required)
* [Project Structure](#project-structure)
* [Project Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [API Routes](#api-routes)

Technology Required
--------------------
* Python 3.11.0

Project Structure
-----------------

* `Models`: Models used in the project
    * `CropRecommedation`: Model and Scaler for crop recommendation
    * `CropDiseaseDetection`: Model and Class Indices for crop disease detection
* `CropRecommendation`: CropRecommendation modules
* `CropDisease`: CropDiseaseDetection modules
* `Gemini`: Gemini Connectivity modules
* `Database`: Database modules
* `app.py`: Main application file

Project Features
-----------------

* `Current Weather`: Provides real-time weather data for a specific location, including temperature, humidity, and wind speed.
* `Weather Forcasting`: Provides 7-day weather forecasts for a specific location, including temperature, humidity, and wind speed.
* `Crop Recommendation`: Recommends suitable crops based on weather conditions, soil type, and other geographical features.
* `Crop Disease Detection`: Detects crop diseases based on images of the crops, using machine learning models

Installation
------------

To install the required python dependencies, run the following command:

```bash
python -m venv env
```
```bash
.\env\Scripts\activate
```
```bash
pip install -r requirements.txt
```

Usage
-----

To use the project, follow these steps:

1. Activate the Virtual Environment: 
```bash
.\env\Scripts\activate
```
2. Run the project: 
```bash
python app.py
```

API Routes
------------

* Register User
API:
```bash
<Host>:8080/api/register_user
```

Request:
```bash
{
    "email": "<String>",
    "password": "<String>",
    "name": "<String>"
}
```

Response:
{
    "success": true/false,
    "message": "<String>"
}

* Login User
API:
```bash
<Host>:8080/api/login_user
```

Request:
```bash
{
    "email": "<String>",
    "password": "<String>"
}
```

Response:
{
    "success": true/false,
    "message": "<String>",
    "token": "<String>"
}

* Get User Details
API:
```bash
<Host>:8080/api/get_user
```

Request:
```bash
{
    "token": "<String>"
}
```

Response:
{
    "success": true/false,
    "message": "<message>",
    "user": "<Array>" #[email, name, gender, phoneNo, location, dob, registered_on]
}

* Update User Details
API:
```bash
<Host>:8080/api/update_user
```

Request:
```bash
{
    "email": "<String>",
    "name": "<String>",
    "gender": "<String -> Male/Female/Other>",
    "phoneNo": "<String>",
    "dob": "<DD-MM-YYYY>",
    "location": "<String>"
}
```

Response:
{
    "success": true/false,
    "message": "<String>",
}

* Crop Recommendation
API:
```bash
<Host>:8080/api/crop_recommendation
```

Request:
```bash
{
    "nitrogen": "<int>",
    "phosphorus": "<int>",
    "potassium": "<int>",
    "temperature": "<float>", 
    "humidity": "<float>",
    "rainfall": "<float>",
    "ph": "<float>"
}
```

Response:
{
    "success": true/false,
    "result": "<String>",
    "explanation": "<String>"
}

* Crop Disease Detection
API:
```bash
<Host>:8080/api/disease_detection
```

Request:
```bash
{
    "file": "<formData -> jpg, png, jepg>",
}
```

Response:
{
    "success": true/false,\n
    "result": "String",\n
    "explanation": "String"
}

