from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from app.model_handler import predict


app = FastAPI(
    title='SberAuto Conversion Prediction API'
)


class SessionData(BaseModel):
    visit_number: int
    utm_source: str
    utm_medium: str
    utm_campaign: str
    utm_adcontent: str
    utm_keyword: str
    device_category: str
    device_os: str
    device_brand: str
    device_screen_resolution: str
    device_browser: str
    geo_country: str
    geo_city: str
    visit_month: int
    visit_day: int
    visit_weekday: int
    visit_hour: int


@app.get('/')
def root():
    return {'message': 'SberAuto conversion prediction API'}


@app.post('/predict')
def get_prediction(data: SessionData):
    input_data = pd.DataFrame([data.model_dump()])

    prediction, probability = predict(input_data)

    return {
        'prediction': int(prediction[0]),
        'probability': round(float(probability[0]), 3)
    }