import joblib
import pandas as pd

from app.preprocessing import preprocess_data


model = joblib.load('models/model.pkl')


def predict(data: pd.DataFrame):
    prepared_data = preprocess_data(data)

    prediction = model.predict(prepared_data)
    probability = model.predict_proba(prepared_data)[:, 1]

    return prediction, probability