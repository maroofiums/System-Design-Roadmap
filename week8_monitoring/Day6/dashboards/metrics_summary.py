import pandas as pd

    
    
def compute_request_metrics(threshold = 0.002):

    df = pd.read_csv("data/metrics.csv")

    latencies = df['latency']

    avg_latency = latencies.mean()
    
    min_latency = latencies.min()
    
    max_latency = latencies.max()

    failed_requests = df[
        df["status"] == "failed"
    ]


    slow_requests = df[
        latencies > threshold
    ]
    


    return_data = {
        "total_requests":df.shape[0],
        "average_latency":avg_latency,
        "min_latency":min_latency,
        "max_latency":max_latency,
        "failed_requests":len(failed_requests),
        "slow_requests":len(slow_requests)
    }

    return return_data

if __name__ == "__main__":

    latency_metrics = compute_request_metrics()

    print(f"Total Requests: {latency_metrics['total_requests']}")
    print(f"Average Latency: {latency_metrics['average_latency']}")
    print(f"Min Latency: {latency_metrics['min_latency']}")
    print(f"Max Latency: {latency_metrics['max_latency']}")
    print(f"Failed Requests: {latency_metrics['failed_requests']}")
    print(f"Slow Requests: {latency_metrics['slow_requests']}")