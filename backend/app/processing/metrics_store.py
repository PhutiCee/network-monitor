from collections import defaultdict, deque
import time
import threading

class MetricsStore:
    def __init__(self):
        self.lock = threading.Lock()

        # store (timestamp, size)
        self.bandwidth = deque(maxlen=1000)

        self.protocols = defaultdict(int)
        self.talkers = defaultdict(int)
        self.connections = 0

    def update(self, packet):
        now = time.time()

        with self.lock:
            # store raw event
            self.bandwidth.append((now, packet.size))

            self.protocols[packet.protocol] += 1
            self.talkers[packet.src_ip] += packet.size
            self.talkers[packet.dst_ip] += packet.size
            self.connections += 1

    # NEW: bytes per second (last 10 seconds)
    def get_bandwidth_rate(self, window=10):
        now = time.time()

        with self.lock:
            total = sum(
                size for t, size in self.bandwidth
                if now - t <= window
            )

        return total / window

    def get_packets_per_second(self, window=10):
        now = time.time()

        with self.lock:
            count = sum(
                1 for t, _ in self.bandwidth
                if now - t <= window
            )

        return count / window

    def snapshot(self):
        with self.lock:
            top_talkers = dict(
                sorted(self.talkers.items(), key=lambda x: x[1], reverse=True)[:10]
            )

        return {
            "connections": self.connections,
            "protocols": dict(self.protocols),
            "top_talkers": top_talkers,

            # NEW METRICS
            "bandwidth": list(self.bandwidth),
            "bandwidth_rate": self.get_bandwidth_rate(),
            "pps": self.get_packets_per_second()
        }