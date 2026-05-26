import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

train_df = pd.read_csv("train.csv")

X_train = train_df[["feature"]]
y_train = train_df["label"]

model = LogisticRegression()

model.fit(X_train,y_train)

prod_df = pd.read_csv("production.csv")

X_prod = prod_df[["feature"]]
y_prod = prod_df["label"]

prediction = model.predict(X_prod)

accuracy = accuracy_score(
    y_prod,prediction
)

print(f"Accuracy: {accuracy:.2f}")

# Drift detection threshold
threshold = 0.60

if accuracy < threshold:
    print("\nWARNING: Concept Drift Detected")
else:
    print("\nModel Performance Stable")

accuracies = [
    0.95,
    0.93,
    0.90,
    0.82,
    0.75
]

rolling_accuracy = (
    sum(accuracies) / len(accuracies)
)

print(
    f"Rolling Accuracy: {rolling_accuracy}"
)