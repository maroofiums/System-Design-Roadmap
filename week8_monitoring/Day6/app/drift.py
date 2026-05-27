import pandas as pd
from scipy.stats import  ks_2samp

def detect_drift():
    train_df = pd.read_csv(
        "data/train.csv"
    )
    
    production_df = pd.read_csv(
        "data/production.csv"
    )

    train_feature = train_df["feature"]

    production_feature = production_df["feature"]

    statistic, p_value = ks_2samp(
        train_feature,
        production_feature
    )

    if p_value < 0.05:
        
        return "WARNING: Data Drift Detected"

    return "No significant drift"