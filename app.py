import uvicorn
from fastapi import FastAPI
from main import cancer
import pandas as pd 
import numpy as np 
import pickle

app = FastAPI()

def predictCancer(data):

    data1 = {
    'GENDER': [float(data['GENDER'])],
    'AGE': [float(data['AGE'])],
    'SMOKING': [float(data['SMOKING'])],
    'YELLOW_FINGERS': [float(data['YELLOW_FINGERS'])],
    'ANXIETY': [float(data['ANXIETY'])],
    'PEER_PRESSURE': [float(data['PEER_PRESSURE'])],
    'CHRONIC DISEASE': [float(data['CHRONIC_DISEASE'])],
    'FATIGUE': [float(data['FATIGUE'])],
    'ALLERGY': [float(data['ALLERGY'])],
    'WHEEZING': [float(data['WHEEZING'])],
    'ALCOHOL CONSUMING': [float(data['ALCOHOL_CONSUMING'])],
    'COUGHING': [float(data['COUGHING'])],
    'SHORTNESS OF BREATH': [float(data['SHORTNESS_OF_BREATH'])],
    'SWALLOWING DIFFICULTY': [float(data['SWALLOWING_DIFFICULTY'])],
    'CHEST PAIN': [float(data['CHEST_PAIN'])]
    }

    # import scaler
    with open('scaler.pkl', 'rb') as file:
        scaler1 = pickle.load(file)

    df2 = pd.DataFrame(data1)
    record_to_scale = df2.iloc[0:1]
    print("before std",df2)
    num_vars=['AGE']
    df2[num_vars]=scaler1.transform(record_to_scale[num_vars])
    print("Standardized record",df2)
    single_sample = np.array(df2).reshape(1, -1)
    print(single_sample)
    #import model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    prediction= model.predict(single_sample)
    print('prediction FROM FN',prediction)
    return prediction


@app.get('/')
def index():
    return {'message': 'Cancer Prediction ML API'}

@app.post('/cancer/predict')
def predict_lung_cancer(data:cancer):
    if(data):
        data = data.dict()
        prediction = predictCancer(data)
        python_list = prediction.tolist()
        print('prediction',type(python_list))
        return {
            'prediction': python_list[0]
        }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)