from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.feedback.feedback_utils import get_positive_feedback_prediction_ids
from app.db.database import get_db
from app.auth.auth_dependency import admin_required
from app.db.models import Prediction, Feedback


def get_positive_feedback_predictions(
    current_user: dict = Depends(admin_required),
    db: Session = Depends(get_db)
):

    try:

        prediction_ids = get_positive_feedback_prediction_ids(db)

        return {
            "success": True,
            "count": len(prediction_ids),
            "prediction_ids": prediction_ids
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )