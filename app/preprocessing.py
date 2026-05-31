import pandas as pd
import joblib


encoder = joblib.load('models/encoder.pkl')


cat_cols = [
    'utm_source',
    'utm_medium',
    'utm_campaign',
    'utm_adcontent',
    'utm_keyword',
    'device_category',
    'device_os',
    'device_brand',
    'device_screen_resolution',
    'device_browser',
    'geo_country',
    'geo_city'
]


def preprocess_data(data: pd.DataFrame):

    data = data.copy()

    data[cat_cols] = encoder.transform(
        data[cat_cols]
    )

    return data