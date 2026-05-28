import pandas as pd
import os
import time

METRICS_FILE = "logs/metrics.csv"

def run_dashboard():
    print("=========================================")
    print("📊 Live Performance Monitoring Dashboard")
    print("=========================================\n")
    
    if not os.path.exists(METRICS_FILE):
        print("Waiting for traffic to generate metrics files...")
        return

    try:
        df = pd.read_csv(METRICS_FILE)
        if df.empty:
            print("No entries located in metrics databases.")
            return

        total_requests = len(df)
        avg_latency = df['latency'].mean() * 1000 # Convert to ms
        p95_latency = df['latency'].quantile(0.95) * 1000
        error_rate = (df['status_code'] != 200).mean() * 100

        print(f"⏱️ Total Handled Requests : {total_requests}")
        print(f"⚡ Average API Latency     : {avg_latency:.2f} ms")
        print(f"🚀 95th Percentile Latency : {p95_latency:.2f} ms")
        print(f"❌ System Error Rate       : {error_rate:.2f}%")
        
        # Highlight anomalous latencies
        slow_queries = df[df['latency'] > 0.100]
        if not slow_queries.empty:
            print(f"⚠️ Alert: {len(slow_queries)} requests breached the 100ms SLA.")

    except Exception as e:
        print(f"Critical error rendering runtime analytics: {e}")

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        run_dashboard()
        time.sleep(5)