import os
import pandas as pd

from fastapi import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Prediction, RetrainingLog
from app.feedback.feedback_utils import (
    get_positive_feedback_prediction_ids
)

from app.config import RETRAINING_DATA_PATH


def add_data_from_positive_feedback(
    db: Session = Depends(get_db)
):

    try:

        # GET POSITIVE FEEDBACK PREDICTION IDS
        prediction_ids = (
            get_positive_feedback_prediction_ids(db)
        )

        # GET ALREADY RETRAINED IDS
        retrained_ids = db.query(
            RetrainingLog.prediction_id
        ).all()

        retrained_ids = [
            id[0]
            for id in retrained_ids
        ]

        # FILTER NEW IDS
        filtered_prediction_ids = [
            pid for pid in prediction_ids
            if pid not in retrained_ids
        ]

        # FETCH ONLY NEW PREDICTIONS
        predictions = db.query(Prediction).filter(
            Prediction.id.in_(filtered_prediction_ids)
        ).all()

        print(f"Predictions: {predictions}")

        training_data = []

        for prediction in predictions:

            training_data.append({
                "customerID": 0,
                "gender": prediction.gender,
                "SeniorCitizen": prediction.SeniorCitizen,
                "Partner": prediction.Partner,
                "Dependents": prediction.Dependents,
                "tenure": prediction.tenure,
                "PhoneService": prediction.PhoneService,
                "MultipleLines": prediction.MultipleLines,
                "InternetService": prediction.InternetService,
                "OnlineSecurity": prediction.OnlineSecurity,
                "OnlineBackup": prediction.OnlineBackup,
                "DeviceProtection": prediction.DeviceProtection,
                "TechSupport": prediction.TechSupport,
                "StreamingTV": prediction.StreamingTV,
                "StreamingMovies": prediction.StreamingMovies,
                "Contract": prediction.Contract,
                "PaperlessBilling": prediction.PaperlessBilling,
                "PaymentMethod": prediction.PaymentMethod,
                "MonthlyCharges": prediction.MonthlyCharges,
                "TotalCharges": 0,

                "Churn": (
                    "Yes"
                    if prediction.prediction == 1
                    else "No"
                )
            })

        # CREATE DATAFRAME
        df = pd.DataFrame(training_data)

        # CHECK FILE EXISTENCE
        file_exists = os.path.exists(
            RETRAINING_DATA_PATH
        )

        # APPEND TO CSV
        df.to_csv(
            RETRAINING_DATA_PATH,
            mode='a',
            header=not file_exists,
            index=False
        )

        # CREATE RETRAINING LOGS
        for prediction in predictions:

            retraining_log = RetrainingLog(
                prediction_id=prediction.id
            )

            db.add(retraining_log)

        db.commit()

        return {
            "success": True,
            "message": (
                "Training data added successfully"
            ),
            "rows_added": len(training_data)
        }

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Retraining failed: {str(e)}"
        )