from fastapi import Depends
from sqlalchemy.orm import Session
from app.auth.auth_dependency import user_required
from app.db.database import get_db
from app.prediction.predict import predict_customer
from app.schema.model_schema import CustomerInput


def predict(
    request: CustomerInput,
    db: Session = Depends(get_db),
    current_user: dict = Depends(user_required)):

    user_id = current_user["id"]

    return predict_customer(
        request=request,
        db=db,
        user_id=user_id
    )