from sklearn.ensemble import RandomForestClassifier

def train_model(X_train,y_train):
    params = {
        'n_estimators': 100,
        'max_depth': None,
        'min_samples_split': 2,
        'min_samples_leaf': 1,
        'random_state': 42
    }

    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    return model,params