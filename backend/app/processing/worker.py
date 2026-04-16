import threading
from app.processing.aggregator import packet_queue
from app.processing.store_instance import metrics_store  # IMPORTANT FIX

def worker():
    print("Worker started...")

    while True:
        packet = packet_queue.get()

        # print("WORKER RECEIVED:", packet)

        metrics_store.update(packet)

        packet_queue.task_done()


def start_worker():
    t = threading.Thread(target=worker, daemon=True)
    t.start()