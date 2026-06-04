from apscheduler.schedulers.blocking import BlockingScheduler

from pipeline.retrain import retrain_model

scheduler = BlockingScheduler()


@scheduler.scheduled_job(
    "interval",
    minutes=1
)
def scheduled_training():

    print("\nStarting Retraining\n")

    retrain_model()

    print("\nRetraining Finished\n")


scheduler.start()