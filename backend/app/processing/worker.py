from app.processing.alert_engine import AlertEngine
from app.processing.store_instance import metrics_store
from app.processing.aggregator import packet_queue
import threading

alert_engine = AlertEngine()

def worker():
    print("Worker started...")

    while True:
        packet = packet_queue.get()

        if packet:
            metrics_store.update(packet)
            alert_engine.process(packet)  

        packet_queue.task_done()


def get_alert_engine():
    return alert_engine


def start_worker():
    t = threading.Thread(target=worker, daemon=True)
    t.start()