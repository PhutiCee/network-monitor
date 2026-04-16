from fastapi import FastAPI
from app.api.stats import router as stats_router
from app.processing.worker import start_worker
from app.capture.sniffer import start_sniffing
import threading

app = FastAPI()
app.include_router(stats_router)

@app.on_event("startup")
def startup_event():
    print("Starting background services...")

    start_worker()

    # Run sniffer in a thread (VERY IMPORTANT)
    threading.Thread(
        target=start_sniffing,
        args=("Wi-Fi",),
        daemon=True
    ).start()


@app.get("/")
def root():
    return {"status": "Running"}