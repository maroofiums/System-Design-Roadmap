from src.data_loader import load_data


def test_data_loading():

    X_train, X_test, y_train, y_test = load_data()

    assert len(X_train) > 0
    assert len(X_test) > 0

    assert X_train.shape[1] == 4