import scapy.all as scapy

class PacketSniffer:
    def __init__(self):
        pass

    def start_sniffing(self):
        """Start sniffing packets on the network."""
        print("Starting packet sniffing...")
        scapy.sniff(prn=self.process_packet, store=False)

    def process_packet(self, packet):
        """Process and display the packet information."""
        print(packet.summary())

if __name__ == "__main__":
    # Example usage
    sniffer = PacketSniffer()
    sniffer.start_sniffing()
