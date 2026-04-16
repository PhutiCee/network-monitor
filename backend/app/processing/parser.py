from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6
from datetime import datetime
from app.models.packet_model import PacketModel


def parse_packet(packet):
    try:
        ip_layer = None
        protocol = "OTHER"

        # IPv4
        if packet.haslayer(IP):
            ip_layer = packet[IP]

        # IPv6 support (IMPORTANT on Windows)
        elif packet.haslayer(IPv6):
            ip_layer = packet[IPv6]

        else:
            return None  # still ignore non-IP safely

        # protocol detection
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

    except Exception as e:
        print("Parser error:", e)
        return None