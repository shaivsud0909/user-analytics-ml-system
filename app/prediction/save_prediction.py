from sqlalchemy.orm import Session

from app.db.models import Prediction
from app.schema.model_schema import CustomerInput


def save_prediction(
    db: Session,
    user_id: int,
    request: CustomerInput,
    prediction: int,
    probability: float
):

    prediction_data = Prediction(

        user_id=user_id,

        gender=request.gender,
        SeniorCitizen=request.SeniorCitizen,
        Partner=request.Partner,
        Dependents=request.Dependents,
        tenure=request.tenure,
        PhoneService=request.PhoneService,
        MultipleLines=request.MultipleLines,
        InternetService=request.InternetService,
        OnlineSecurity=request.OnlineSecurity,
        OnlineBackup=request.OnlineBackup,
        DeviceProtection=request.DeviceProtection,
        TechSupport=request.TechSupport,
        StreamingTV=request.StreamingTV,
        StreamingMovies=request.StreamingMovies,
        Contract=request.Contract,
        PaperlessBilling=request.PaperlessBilling,
        PaymentMethod=request.PaymentMethod,
        MonthlyCharges=request.MonthlyCharges,

        prediction=prediction,

        probability=round(
            float(probability),
            4
        )
    )

    db.add(prediction_data)

    db.commit()

    db.refresh(prediction_data)

    return prediction_data