Project Overview
===============

This project aims to develop a smart farming backend using Python, focusing on creating a scalable and efficient system for multiple useful operatins. It is designed to be used in conjunction with a frontend application, which will handle user interactions and display data to the user. The project provides API endpoints for different smart farming operations.

Table of Contents
-----------------

* [Project Structure](#project-structure)
* [Project Features](#features)
* [Installation](#installation)
* [Usage](#usage)

Project Structure
-----------------

* `Models`: Models used in the project
    * `CropRecommedation`: Model and Scaler for crop recommendation
* `CropRecommendation`: CropRecommendation modules
* `Gemini`: Gemini Connectivity modules

Project Features
-----------------

* `Current Weather`: Provides real-time weather data for a specific location, including temperature, humidity, and wind speed.
* `Weather Forcasting`: Provides 7-day weather forecasts for a specific location, including temperature, humidity, and wind speed.
* `Crop Recommendation`: Recommends suitable crops based on weather conditions, soil type, and other geographical features.

Installation
------------

To install the required python dependencies, run the following command:

```bash
pip install -r requirements.txt
```

Usage
-----

To use the project, follow these steps:

1. Run the project: `python app.py`
