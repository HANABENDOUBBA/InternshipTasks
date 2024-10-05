from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
import datetime
def analyze_packet(packet):
    if IP in packet:
        ip_layer=packet[IP]
        src_ip=ip_layer.src
        dst_ip=ip_layer.dst
        protocol=ip_layer.proto
    proto='OTHER'
    if protocol==6:
        proto='TCP'
    elif protocol==17:
        proto=='UDP'    
    elif protocol==1:
        proto='ICMP'

        
    payload_len=len(packet[IP].payload)
    timestamp=datetime.datetime.now()
    print(f"\n[{timestamp}]")
    print(f"Protocol:{proto}")
    print(f"Source IP: {src_ip}")
    print(f" Destination IP: {dst_ip}")
    print(f"Payload Length: {payload_len}")
    if proto=='TCP'and TCP in packet:
        tcp_layer=packet[TCP]
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")
    if proto=='UDP' and UDP in packet:
        udp_layer=packet[UDP]
        print(f"Source Port: {udp_layer.sport}")
        print(f"Destination Port: {udp_layer.dport}")


def start_sniffing():  
  print("Starting packet capture. Press Ctrl+C to stop.")
  sniff(prn=analyze_packet, store=False,iface="Wi-Fi")


if __name__ == "__main__":
    start_sniffing()



           