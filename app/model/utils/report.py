from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import pandas as pd


def generate_report(model, X_test, y_test):

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Classification report
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report_dict).transpose()

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    cm_df = pd.DataFrame(
        cm,
        index=["Actual 0", "Actual 1"],
        columns=["Predicted 0", "Predicted 1"]
    )

    # ROC-AUC
    roc = roc_auc_score(y_test, y_prob)


    return {
        "classification_report": report_df,
        "confusion_matrix": cm_df,
        "roc_auc": roc
    }