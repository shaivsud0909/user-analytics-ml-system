from app.db.models import Prediction,Feedback
from sqlalchemy.orm import Session
from fastapi import HTTPException

def validate_prediction_access(
    prediction_id: int,
    user_id: int,
    db: Session
):

    prediction = db.query(Prediction).filter(
        Prediction.id == prediction_id
    ).first()

    if not prediction:
        raise HTTPException(
            status_code=404,
            detail="Prediction not found"
        )

    if prediction.user_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="Unauthorized"
        )

    return prediction



def create_feedback(
    prediction_id: int,
    rating: int,
    is_correct: bool,
    db: Session
):

    # CHECK FEEDBACK ALREADY EXISTS
    existing_feedback = db.query(Feedback).filter(
        Feedback.prediction_id == prediction_id
    ).first()

    if existing_feedback:
        raise HTTPException(
            status_code=400,
            detail="Feedback already submitted"
        )

    # CREATE FEEDBACK OBJECT
    feedback = Feedback(
        prediction_id=prediction_id,
        rating=rating,
        is_correct=is_correct
    )

    return feedback
