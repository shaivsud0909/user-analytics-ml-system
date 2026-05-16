from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.auth_dependency import user_required
from app.db.database import get_db

from app.feedback.feedback_utils import create_feedback, validate_prediction_access
from app.schema.feedback_schema import FeedbackRequest


def add_feedback(
    prediction_id: int,
    request: FeedbackRequest,
    current_user: dict = Depends(user_required),
    db: Session = Depends(get_db)
):
    try:

        user_id = current_user["id"]

        rating = request.rating
        is_correct = request.is_correct

        #fetch prediction
        prediction = validate_prediction_access(
                prediction_id=prediction_id,
                user_id=user_id,
                db=db
            )
        
        #create feedback object
        feedback = create_feedback(
            prediction_id=prediction_id,
            rating=rating,
            is_correct=is_correct,
            db=db
        )
 

        # SAVE TO DB
        db.add(feedback)
        db.commit()
        db.refresh(feedback)

        return {
            "success": True,
            "message": "Feedback submitted successfully",
            "feedback_id": feedback.id
        }
    
    except HTTPException as http_error:
        raise http_error

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )