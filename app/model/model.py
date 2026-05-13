import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from app.model.utils.cleaning import clean_csv
from app.config import CSV_FILE_PATH
from app.model.utils.hyper_parameter import tune_hyperparameters
from app.model.utils.report import generate_report
import joblib
from app.config import MODEL_PATH

def model_training():

    df= pd.read_csv(CSV_FILE_PATH)

    #cleaning the data
    df=clean_csv(df)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    )

    numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns
    categorical_cols = X.select_dtypes(include=["object"]).columns

    #scaling and encoding the data
    preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_cols),
        ("cat", OneHotEncoder(drop="first",handle_unknown="ignore"), categorical_cols)
    ]
    )

    #xgb model with some initial hyperparameters
    xgb_model = XGBClassifier(
    objective="binary:logistic",
    eval_metric="logloss",
    scale_pos_weight=2.8,
    random_state=42
    )
    
    #pipeline for preprocessing and modeling
    pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", xgb_model)
    ])

    #tuning the hyperparameters using grid search
    model = tune_hyperparameters(pipeline, X_train, y_train)

    #training the model with the best hyperparameters
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    report = generate_report(model, X_test, y_test)

    return {
        "message": "Model trained successfully",
        "roc_auc": report["roc_auc"]
    }