import pandas as pd
from scipy.stats import ks_2samp

train_df = pd.read_csv(
    "train.csv"
)
production_df = pd.read_csv(
    "production.csv"
)

train_age = train_df["age"]
production_age = production_df["age"]

train_mean = train_age.mean()
production_mean = production_age.mean()

print(
    f"Train Mean: {train_mean}"
)
print(
    f"Production Mean: {production_mean}"
)

train_var = train_age.var()
production_var = production_age.var()

print(
    f"Train Variance: {train_var}"
)
print(
    f"Production Variance: {production_var}"
)

statistic,p_value = ks_2samp(
    train_age,
    production_age
)

print(f"\nKS Statistic: {statistic}")

print(f"P-Value: {p_value}")

# Drift detection
if p_value < 0.05:

    print("\nWARNING: Data Drift Detected")

else:

    print("\nNo significant drift detected")