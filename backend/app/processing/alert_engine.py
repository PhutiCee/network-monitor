import time
from collections import defaultdict, deque

class AlertEngine:
    def __init__(self):
        self.bandwidth_window = deque(maxlen=50)
        self.ip_activity = defaultdict(int) 

        self.alerts = deque(maxlen=20)

        # thresholds (tune later)
        self.BANDWIDTH_THRESHOLD = 50000  # bytes/sec
        self.IP_THRESHOLD = 200000        # bytes total

    def process(self, packet):
        now = time.time()

        # track bandwidth
        self.bandwidth_window.append((now, packet.size))

        # track IP activity
        self.ip_activity[packet.src_ip] += packet.size

        self.check_bandwidth_alert()
        self.check_ip_anomaly(packet.src_ip)

    # 1. Traffic spike detection
    def check_bandwidth_alert(self):
        now = time.time()

        total = sum(size for t, size in self.bandwidth_window if now - t <= 5)

        if total > self.BANDWIDTH_THRESHOLD:
            self.add_alert(
                f"🚨 High traffic spike detected: {total} bytes/5s"
            )

    # 2. Unusual IP activity detection
    def check_ip_anomaly(self, ip):
        if self.ip_activity[ip] > self.IP_THRESHOLD:
            self.add_alert(
                f"⚠️ Unusual IP activity: {ip} exceeded threshold"
            )

    def add_alert(self, message):
        self.alerts.append({
            "message": message,
            "timestamp": time.time()
        })

        print("ALERT:", message)

    def get_alerts(self):
        return list(self.alerts)