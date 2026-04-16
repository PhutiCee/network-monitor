from scapy.all import sniff
from app.processing.parser import parse_packet
from app.processing.aggregator import packet_queue

def process_packet(packet):
    print("RAW:", packet.summary())

    parsed = parse_packet(packet)


    if parsed:
        # print("PARSED:", parsed)   
        packet_queue.put(parsed)


def start_sniffing(interface=None):
    print("Starting packet capture...")

    sniff(
        iface=interface,
        prn=process_packet,
        store=False
    )