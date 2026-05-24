import pandas as pd

df = pd.read_csv("prediction_logs.csv")

average_latency = df["latency"].mean()

print(f"Average Latency: {average_latency:.6f} sec")

threshold = 0.002

slow_requests = df[
    df["latency"] > threshold
]

print("\nSlow Requests:")

print(slow_requests)