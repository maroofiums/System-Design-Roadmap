import numpy as np
import pandas as pd
from scipy.stats import ks_2samp
import os
from app.logger import logger

# Generate dummy reference baseline data simulating physical features (e.g., house size, age)
np.random.seed(42)
BASELINE_DATA = pd.DataFrame({
    'feature1': np.random.normal(loc=50, scale=10, size=1000),
    'feature2': np.random.normal(loc=25, scale=5, size=1000)
})

def check_data_drift() -> dict:
    """
    Reads the runtime prediction logs and runs a Kolmogorov-Smirnov (KS) test 
    against the baseline training data distribution.
    """
    pred_log_path = "logs/prediction.log"
    if not os.path.exists(pred_log_path) or os.path.getsize(pred_log_path) == 0:
        return {"status": "insufficient_data", "drift_detected": False}
    
    try:
        # Load logged production features
        df = pd.read_csv(pred_log_path, names=["timestamp", "feature1", "feature2", "prediction"])
        
        # We need a statistical window to reliably calculate drift
        if len(df) < 30:
            return {"status": "collecting_data", "count": len(df), "drift_detected": False}
        
        # Pull the most recent 200 entries for windowed distribution checking
        recent_data = df.tail(200)
        drift_results = {}
        drift_detected = False
        
        for col in ['feature1', 'feature2']:
            # Run KS Test. If p-value < 0.05, we reject the null hypothesis (distributions differ)
            stat, p_value = ks_2samp(BASELINE_DATA[col], recent_data[col])
            is_drifted = p_value < 0.05
            drift_results[col] = {"p_value": float(p_value), "drift": is_drifted}
            
            if is_drifted:
                drift_detected = True
                logger.warning(f"🚨 DATA DRIFT DETECTED on column '{col}'! p-value: {p_value:.4f}")
                
        return {"status": "success", "drift_detected": drift_detected, "metrics": drift_results}
        
    except Exception as e:
        logger.error(f"Failed to calculate data drift: {str(e)}")
        return {"status": "error", "message": str(e), "drift_detected": False}