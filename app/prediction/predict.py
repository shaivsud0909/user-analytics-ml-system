from app.schema.model_schema import CustomerInput
from app.config import MODEL_PATH
import joblib
import pandas as pd
from app.prediction.save_prediction import save_prediction
from sqlalchemy.orm import Session

model = joblib.load(MODEL_PATH)


def predict_customer(
    request: CustomerInput,
    db: Session,
    user_id: int
):

    try:

        # request -> dataframe
        input_data = request.model_dump()

        df = pd.DataFrame([input_data])

        # model prediction
        prediction = model.predict(df)[0]

        # prediction probability
        probability = model.predict_proba(df)[0][1]

        # save prediction in database
        saved_prediction = save_prediction(
            db=db,
            user_id=user_id,
            request=request,
            prediction=int(prediction),
            probability=float(probability)
        )

        # response
        return {
            "prediction_id": saved_prediction.id,
            "prediction": int(prediction),
            "churn": "Yes" if prediction == 1 else "No",
            "probability": round(float(probability), 4)
        }

    except Exception as e:

        db.rollback()

        return {
            "error": str(e)
        }