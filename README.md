# Lung Cancer Prediction FastAPI App

This FastAPI application predicts the likelihood of lung cancer based on a list of symptoms provided by the user. It exposes two endpoints:
- **GET** endpoint: Provides general information for test the app.
- **POST** endpoint: Accepts a list of symptoms and responds with a prediction of whether the person has lung cancer or not.

The application is built using FastAPI and Uvicorn for fast, asynchronous performance. A `requirements.txt` file is included to manage dependencies.

## Features

- **FastAPI** for handling requests.
- **POST** endpoint to predict lung cancer based on symptoms.
- **GET** endpoint for general application information.
- Lightweight and easy to set up with `uvicorn`.

## Endpoints

### 1. GET `/`
- Provides a welcome message or basic information about the application.

### 2. POST `/predict`
- Accepts a JSON payload containing a list of symptoms and returns whether the person has cancer or not.

(YES=2 , NO=1.)
(Female=2 , Male=1.)

#### Sample Request:
{
  "GENDER": ,
  "AGE": 0,
  "SMOKING": 0,
  "YELLOW_FINGERS": 0,
  "ANXIETY": 0,
  "PEER_PRESSURE": 0,
  "CHRONIC_DISEASE": 0,
  "FATIGUE": 0,
  "ALLERGY": 0,
  "WHEEZING": 0,
  "ALCOHOL_CONSUMING": 0,
  "COUGHING": 0,
  "SHORTNESS_OF_BREATH": 0,
  "SWALLOWING_DIFFICULTY": 0,
  "CHEST_PAIN": 0
}

#### Sample Response:
{"message":"Cancer Prediction ML API"}

## Installation and Running the App

### 1. Clone the Repository
git clone https://github.com/WaruniSH/lung-cancer-prediction-fastapi.git
cd lung-cancer-prediction-fastapi

### 2. Create a Virtual Environment
It’s recommended to create a virtual environment to keep dependencies isolated.

python -m venv venv
source venv/bin/activate 

### 3. Install Requirements
Install the necessary packages from the requirements.txt file.

pip install -r requirements.txt

### 4. Run the Application
Use Uvicorn to run the FastAPI application.

uvicorn app:app --reload

### 5. Test the Endpoints
GET Endpoint: Visit http://127.0.0.1:8000/ on your browser or using a tool like curl or Postman.

POST Endpoint: Send a POST request to http://127.0.0.1:8000/predict with a JSON body containing the symptoms.

### Medium Article Link : 
https://medium.com/@warunisha1/how-to-deploy-a-fastapi-deep-learning-application-in-render-e945aa7f6d2a

