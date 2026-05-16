from sklearn.model_selection import GridSearchCV

def tune_hyperparameters(pipeline, X_train, y_train):

    param_grid = {
        "model__n_estimators": [100, 200, 300, 400],
        "model__learning_rate": [0.03, 0.05, 0.1],
        "model__max_depth": [3, 5, 7],
        "model__min_child_weight": [1, 3],
        "model__subsample": [0.8, 1.0],
        "model__colsample_bytree": [0.8, 1.0]
    }

    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        scoring="recall",   # important for churn
        cv=3,
        verbose=1,
        n_jobs=-1
    )

    grid_search.fit(X_train, y_train)

    print("Best Params:", grid_search.best_params_)
    print("Best Score:", grid_search.best_score_)

    return grid_search.best_estimator_