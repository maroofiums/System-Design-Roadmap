from apscheduler.schedulers.blocking import BlockingScheduler
import time

last_retraining_time = None


def latency(func):
    def wrapper():
        global last_retraining_time

        current_time = time.time()

        if last_retraining_time is not None:
            gap = current_time - last_retraining_time
            print(f"\nTime Since Last Retraining: {gap:.2f} sec")

        last_retraining_time = current_time

        start = time.time()

        func()

        end = time.time()

        execution_time = end - start

        print(f"Training Took {execution_time:.2f} sec To Run!\n")

    return wrapper


@latency
def train_pipeline():
    print("Loading Data...")
    time.sleep(1)

    print("Training Model...")
    time.sleep(2)

    print("Saving Model...")
    time.sleep(1)

    print("Training Complete")


scheduler = BlockingScheduler()


@scheduler.scheduled_job("interval", minutes=0.1)
def retraining_loop():
    train_pipeline()


scheduler.start()