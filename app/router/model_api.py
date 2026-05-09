from fastapi import APIRouter
from app.prediction.precdict import model_prediction

user_router = APIRouter()

user_router.post("/predict")(model_prediction)

