# SberAuto Conversion Prediction API

## Описание проекта

Компания «СберАвтоподписка» хочет увеличить эффективность сайта: улучшить пользовательский опыт, повысить конверсию, сделать рекламные кампании более результативными. Необходимо создать модель, которая предсказывает вероятность того, что пользователь совершит целевое действие (оставит заявку, закажет звонок и пр.) на сайте.

Эта модель поможет:

- Оценивать эффективность каналов привлечения трафика;

- Адаптировать рекламные кампании;

- Улучшать UX сайта за счет анализа поведения пользователей.

## Структура проекта

```text
sberauto_conversion_project/
│
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── model_handler.py
│   └── preprocessing.py
│
├── models/
│   └── model.pkl
│   └── encoder.pkl
│
├── examples/
│   ├── sample_request.json
│   └── client.py
│
├── tests/
│   └── test_api.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Описание данных.pdf
└── Проектная_практика(final).ipynb
```

**Exploratory Data Analysis**, обоснование выбора модели, обучение и сохранение модели выполнены в файле Проектная_практика(final).ipynb

Описание признаков и структуры данных приведено в файле "Описание данных.pdf".

В проекте были обучены следующие модели:

- Logistic Regression

- Random Forest

- CatBoost

- LightGBM

Лучший результат показала модель LightGBM.

Итоговое качество модели после подбора гиперпараметров:

ROC-AUC = 0.717

Модель находится по адресу models/model.pkl

Модель была упакована в FastAPI-сервис и контейнеризирована с помощью Docker.
API принимает данные визита в формате, близком к таблице ga_sessions, автоматически выполняет предобработку данных и возвращает прогноз вероятности совершения целевого действия.

## Запуск проекта

Установка зависимостей и локальный запуск:

```bash
pip install -r requirements.txt
uvicorn app.api:app --reload
```

После запуска документация доступна по адресу:

```text
http://127.0.0.1:8000/docs
```

### Docker

Сборка и запуск контейнера:

```bash
docker compose up --build
```

### Пример запроса

POST /predict

```json
{
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
```

Пример ответа:

```json
{
    "prediction": 0,
    "probability": 0.029
}
```
