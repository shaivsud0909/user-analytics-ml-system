from fastapi import APIRouter
from app.model.model import model_training

admin_router = APIRouter()

admin_router.post("/train")(model_training)