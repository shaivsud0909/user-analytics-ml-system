def clean_csv(df):
    # dropping the customerID and TotalCharges columns as they are not useful for prediction
    df = df.drop(columns=['customerID', 'TotalCharges'])

    # converting the target variable 'Churn' to binary values (1 for 'Yes' and 0 for 'No')
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df