from sklearn.metrics import accuracy_score

def monitor_accuracy(
        y_true,
        predictions,
        threshold=0.60
):
    accuracy = accuracy_score(
        y_true,
        predictions
    )

    print(f"Accuracy: {accuracy:.2f}")

    if accuracy < threshold:
        print(
            "WARNING: Concept Drift Detected"
        )

    return accuracy

