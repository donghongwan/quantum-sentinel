import scapy.all as scapy

class ProtocolAnalysis:
    def __init__(self, interface):
        self.interface = interface

    def analyze_protocols(self):
        """Capture and analyze network packets for vulnerabilities."""
        print(f"Analyzing network protocols on interface {self.interface}...")
        scapy.sniff(iface=self.interface, prn=self.process_packet, store=False)

    def process_packet(self, packet):
        """Process each captured packet."""
        if packet.haslayer(scapy.IP):
            ip_layer = packet[scapy.IP]
            print(f"Captured packet: {ip_layer.src} -> {ip_layer.dst} | Protocol: {ip_layer.proto}")

if __name__ == "__main__":
    # Example usage
    interface = "eth0"  # Change to your network interface
    protocol_analyzer = ProtocolAnalysis(interface)
    protocol_analyzer.analyze_protocols()
