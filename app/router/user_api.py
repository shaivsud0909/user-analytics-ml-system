from fastapi import APIRouter
from app.prediction.service import predict
from app.feedback.service import add_feedback

user_router = APIRouter()

user_router.post("/predict")(predict)
user_router.post( "/predictions/{prediction_id}/feedback")(add_feedback)