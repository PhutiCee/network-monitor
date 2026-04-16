from collections import defaultdict, deque
import time
import threading

class MetricsStore:
    def __init__(self):
        self.lock = threading.Lock()

        # bandwidth tracking (time series)
        self.bandwidth = deque(maxlen=100)

        # protocol counts
        self.protocols = defaultdict(int)

        # top talkers
        self.talkers = defaultdict(int)

        # connection count 
        self.connections = 0

    def update(self, packet):
        with self.lock:
            # bandwidth (bytes over time)
            self.bandwidth.append((time.time(), packet.size))

            # protocol stats
            self.protocols[packet.protocol] += 1

            # IP tracking
            self.talkers[packet.src_ip] += packet.size
            self.talkers[packet.dst_ip] += packet.size

            # connection approximation
            self.connections += 1
            # print("UPDATED METRICS:", self.connections)

    def snapshot(self):
        with self.lock:
            return {
                "bandwidth": list(self.bandwidth),
                "protocols": dict(self.protocols),
                "top_talkers": dict(self.talkers),
                "connections": self.connections
            }