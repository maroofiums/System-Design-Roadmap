from apscheduler.schedulers.blocking import BlockingScheduler
from pipeline.retrain import retrain_model

scheduler = BlockingScheduler()

@scheduler.scheduled_job("interval",minutes=0.1)
def retrain_loop():
    print("Retraining Model...",end="\n\n")
    retrain_model()
    print("Model Retrained",end="\n\n")

scheduler.start()