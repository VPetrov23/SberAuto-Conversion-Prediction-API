from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_root():
    response = client.get('/')

    assert response.status_code == 200


def test_predict():
    sample_data = {
        "visit_number": 2,
        "utm_source": "ZpYIoDJMcFzVoPFsHGJL",
        "utm_medium": "banner",
        "utm_campaign": "LEoPHuyFvzoNfnzGgfcd",
        "utm_adcontent": "vCIpmpaGBnIQhyYNkXqp",
        "utm_keyword": "unknown",
        "device_category": "mobile",
        "device_os": "Android",
        "device_brand": "Samsung",
        "device_screen_resolution": "360x720",
        "device_browser": "Chrome",
        "geo_country": "Russia",
        "geo_city": "Moscow",
        "visit_month": 11,
        "visit_day": 24,
        "visit_weekday": 2,
        "visit_hour": 14
    }

    response = client.post(
        '/predict',
        json=sample_data
    )

    assert response.status_code == 200