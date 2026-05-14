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

```text
app/
│
├── auth/
├── db/
├── feedback/
├── model/
├── prediction/
├── schema/
├── routers/
├── utils/