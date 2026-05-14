import os
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Prediction
from app.feedback.feedback_utils import get_positive_feedback_prediction_ids
import pandas as pd
from app.config import RETRAINING_DATA_PATH

def add_data_from_positive_feedback(
    db: Session = Depends(get_db)
):

    prediction_ids = get_positive_feedback_prediction_ids(db)

    # LOGIC TO ADD DATA TO TRAINING SET

    predictions=db.query(Prediction).filter(
        Prediction.id.in_(prediction_ids)
    ).all()

    # PREPARE DATA
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

            "Churn": "Yes" if prediction.prediction == 1 else "No"
        })

    df= pd.DataFrame(training_data) 

    file_exists = os.path.exists(RETRAINING_DATA_PATH)

    df.to_csv(RETRAINING_DATA_PATH,mode='a',header=not file_exists, index=False)

    return {
        "success": True,
        "message": "Training data added successfully",
        "rows_added": len(training_data)
    }


