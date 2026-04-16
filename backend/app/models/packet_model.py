from dataclasses import dataclass
from datetime import datetime

@dataclass
class PacketModel:
    src_ip: str
    dst_ip: str
    protocol: str
    size: int
    timestamp: datetime