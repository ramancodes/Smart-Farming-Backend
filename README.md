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
`.\env\Scripts\activate`
```
2. Run the project: 
```bash
`python app.py`
```
