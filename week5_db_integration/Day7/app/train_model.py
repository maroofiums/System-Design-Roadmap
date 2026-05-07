from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# ---------------------------
# 1. Load Dataset
# ---------------------------
iris = load_iris()

X = iris.data
y = iris.target

# ---------------------------
# 2. Train/Test Split
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------
# 3. Train Model
# ---------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------------------
# 4. Evaluate (Optional but useful)
# ---------------------------
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# ---------------------------
# 5. Save Model
# ---------------------------
model_dir = "app/ml_model"
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, "iris_model.pkl")

with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"Model saved at: {model_path}")