# User Analytics ML System

## Overview

This project is a machine learning powered customer churn prediction system built using FastAPI.

The system allows users to:
- register and login using JWT authentication
- predict customer churn
- submit feedback on prediction quality
- help improve the ML model through retraining datasets

Admins can:
- monitor prediction feedback
- collect high-quality prediction data
- retrain the ML model using validated feedback data

---

# Tech Stack

| Category | Technology |
|---|---|
| Backend Framework | FastAPI |
| Authentication | JWT + bcrypt |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| ML Library | Scikit-learn |
| Data Processing | Pandas |
| Model Type | Logistic Regression / XGBoost |
| API Testing | Swagger UI |
| Migration Tool | Alembic |

---

# Features

## Authentication
- User Signup/Login
- Admin Login
- JWT Token Authentication
- Role-based Authorization
- Password Hashing using bcrypt

---

## Prediction System
- Customer churn prediction
- Prediction probability score
- Prediction history storage
- User-specific predictions

---

## Feedback System
- One-to-one prediction feedback
- User can mark prediction as:
  - Correct
  - Incorrect
- Rating system (1–5)
- Duplicate feedback prevention

---

## Admin Features
- View high-quality predictions
- Filter positive feedback predictions
- Generate retraining datasets
- Append validated data into retraining CSV

---

## ML Pipeline
- CSV preprocessing
- Model training pipeline
- Feedback-driven retraining
- Retraining dataset generation

---

# Project Structure

.
├── alembic
│   ├── __pycache__
│   │   └── env.cpython-313.pyc
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── __pycache__
│       │   ├── 28475abdddf4_update_user_schema.cpython-313.pyc
│       │   ├── 4ab3816a1b86_update_the_table.cpython-313.pyc
│       │   ├── 6ab863e220d7_update_user_schema.cpython-313.pyc
│       │   ├── 8054d0601c84_update_user_schema.cpython-313.pyc
│       │   ├── 97064f6fdfc6_update_user_schema.cpython-313.pyc
│       │   └── a9842d41bf6b_update_the_table.cpython-313.pyc
│       └── a9842d41bf6b_update_the_table.py
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-313.pyc
│   │   ├── config.cpython-313.pyc
│   │   └── main.cpython-313.pyc
│   ├── auth
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── auth_dependency.cpython-313.pyc
│   │   │   ├── service.cpython-313.pyc
│   │   │   └── utils.cpython-313.pyc
│   │   ├── auth_dependency.py
│   │   ├── service.py
│   │   └── utils.py
│   ├── config.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-313.pyc
│   │   │   ├── database.cpython-313.pyc
│   │   │   └── models.cpython-313.pyc
│   │   ├── database.py
│   │   └── models.py
│   ├── feedback
│   │   ├── __pycache__
│   │   │   ├── feedback_utils.cpython-313.pyc
│   │   │   ├── positive_feedback.cpython-313.pyc
│   │   │   └── service.cpython-313.pyc
│   │   ├── feedback_utils.py
│   │   ├── positive_feedback.py
│   │   └── service.py
│   ├── main.py
│   ├── model
│   │   ├── __pycache__
│   │   │   ├── add_data.cpython-313.pyc
│   │   │   └── model.cpython-313.pyc
│   │   ├── add_data.py
│   │   ├── churn_model.pkl
│   │   ├── model.py
│   │   └── utils
│   │       ├── __pycache__
│   │       │   ├── cleaning.cpython-313.pyc
│   │       │   ├── hyper_parameter.cpython-313.pyc
│   │       │   ├── report.cpython-313.pyc
│   │       │   └── train_test_split.cpython-313.pyc
│   │       ├── cleaning.py
│   │       ├── hyper_parameter.py
│   │       └── report.py
│   ├── prediction
│   │   ├── __pycache__
│   │   │   ├── precdict.cpython-313.pyc
│   │   │   ├── predict.cpython-313.pyc
│   │   │   ├── save_prediction.cpython-313.pyc
│   │   │   └── service.cpython-313.pyc
│   │   ├── predict.py
│   │   ├── save_prediction.py
│   │   └── service.py
│   ├── router
│   │   ├── __pycache__
│   │   │   ├── admin_api.cpython-313.pyc
│   │   │   ├── auth_api.cpython-313.pyc
│   │   │   ├── model_api.cpython-313.pyc
│   │   │   └── user_api.cpython-313.pyc
│   │   ├── admin_api.py
│   │   ├── auth_api.py
│   │   └── user_api.py
│   └── schema
│       ├── __pycache__
│       │   ├── auth_schema.cpython-313.pyc
│       │   ├── feedback_schema.cpython-313.pyc
│       │   └── model_schema.cpython-313.pyc
│       ├── auth_schema.py
│       ├── feedback_schema.py
│       └── model_schema.py
├── app.py
├── data
│   ├── retraining_data.csv
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── main.py
├── postman
│   ├── collections
│   │   └── New Collection
│   │       ├── feedback'.request.yaml
│   │       ├── model training.request.yaml
│   │       ├── prediction feedback adding data.request.yaml
│   │       └── prediction.request.yaml
│   ├── environments
│   ├── flows
│   ├── globals
│   │   └── workspace.globals.yaml
│   ├── mocks
│   └── specs
├── pyproject.toml
├── README.md
└── uv.lock