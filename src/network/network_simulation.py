import random
import time

class NetworkSimulation:
    def __init__(self, num_nodes=10):
        self.num_nodes = num_nodes
        self.network = {f"Node {i}": [] for i in range(num_nodes)}

    def simulate_traffic(self):
        """Simulate network traffic between nodes."""
        print("Simulating network traffic...")
        for _ in range(20):  # Simulate 20 traffic events
            src = random.choice(list(self.network.keys()))
            dst = random.choice(list(self.network.keys()))
            if src != dst:
                self.network[src].append(dst)
                print(f"{src} sent data to {dst}")
            time.sleep(1)

    def display_network(self):
        """Display the current state of the network."""
        print("Current network state:")
        for node, connections in self.network.items():
            print(f"{node} -> {', '.join(connections) if connections else 'No connections'}")

if __name__ == "__main__":
    # Example usage
    simulation = NetworkSimulation(num_nodes=5)
    simulation.simulate_traffic()
    simulation.display_network()
