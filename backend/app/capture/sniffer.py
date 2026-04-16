from scapy.all import sniff
from app.processing.parser import parse_packet

def process_packet(packet):
    parsed = parse_packet(packet)

    if parsed:
        print(f"[{parsed.timestamp}] "
              f"{parsed.src_ip} → {parsed.dst_ip} | "
              f"{parsed.protocol} | {parsed.size} bytes")


def start_sniffing(interface=None):
    print("Starting packet capture...")

    sniff(
        iface=interface,
        prn=process_packet,
        store=False
    )