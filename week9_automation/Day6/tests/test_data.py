import numpy as np
from src.data_loader import load_data

def test_data_loader():
    X_train, X_test, y_train, y_test = load_data()
    
    assert X_train is not None, "X_train should not be None"
    assert X_test is not None, "X_test should not be None"
    assert y_train is not None, "y_train should not be None"
    assert y_test is not None, "y_test should not be None"

    assert len(X_train) > 0, "X_train should not be empty"
    assert len(X_test) > 0, "X_test should not be empty"
    assert len(y_train) > 0, "y_train should not be empty"
    assert len(y_test) > 0, "y_test should not be empty"

    assert len(X_train) == len(y_train), "X_train and y_train should have the same number of samples"

    assert len(X_test) == len(y_test), "X_test and y_test should have the same number of samples"

    assert X_train.shape[1] == X_test.shape[1], "X_train and X_test should have the same number of features"
    assert set(np.unique(y_train)) == set(np.unique(y_test)), "y_train and y_test should have the same unique classes"
    