from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    params = {
        "n_estimators": 100,
        "max_depth": None,
        "random_state": 42
    }
    model = RandomForestClassifier(**params)
    
    model.fit(X_train, y_train)
    
    return model,params
