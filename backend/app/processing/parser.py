from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime
from app.models.packet_model import PacketModel

def parse_packet(packet):
    if not packet.haslayer(IP):
        return None

    ip_layer = packet[IP]

    protocol = "OTHER"
    if packet.haslayer(TCP):
        protocol = "TCP"
    elif packet.haslayer(UDP):
        protocol = "UDP"
    elif packet.haslayer(ICMP):
        protocol = "ICMP"

    return PacketModel(
        src_ip=ip_layer.src,
        dst_ip=ip_layer.dst,
        protocol=protocol,
        size=len(packet),
        timestamp=datetime.now()
    )