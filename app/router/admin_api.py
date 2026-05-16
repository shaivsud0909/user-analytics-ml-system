from fastapi import APIRouter
from app.model.model import model_training
from app.feedback.positive_feedback import get_positive_feedback_predictions
from app.model.add_data import add_data_from_positive_feedback

admin_router = APIRouter()

admin_router.post("/train")(model_training)
admin_router.get("/positive-feedback")(get_positive_feedback_predictions)
admin_router.post("/positive-feedback")(add_data_from_positive_feedback)