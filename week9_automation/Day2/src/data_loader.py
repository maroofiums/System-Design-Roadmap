from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def load_data():
    X,y = load_iris(return_X_y=True)

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

