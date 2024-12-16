import nmap
import matplotlib.pyplot as plt
import networkx as nx

class NetworkMapping:
    def __init__(self):
        self.scanner = nmap.PortScanner()

    def scan_network(self, subnet):
        """Scan the network for active hosts."""
        print(f"Scanning network {subnet}...")
        self.scanner.scan(hosts=subnet, arguments='-sn')
        return self.scanner.all_hosts()

    def visualize_network(self, hosts):
        """Visualize the network topology."""
        G = nx.Graph()
        for host in hosts:
            G.add_node(host)
            for port in self.scanner[host]['tcp']:
                G.add_edge(host, f"{host}:{port}")

        plt.figure(figsize=(10, 10))
        nx.draw(G, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_color='black')
        plt.title("Network Topology")
        plt.show()

if __name__ == "__main__":
    # Example usage
    nm = NetworkMapping()
    subnet = "192.168.1.0/24"  # Change to your subnet
    hosts = nm.scan_network(subnet)
    print("Active hosts:", hosts)
    nm.visualize_network(hosts)
