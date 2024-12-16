import psutil
import time

class TrafficMonitor:
    def __init__(self, interval=1):
        self.interval = interval

    def monitor_traffic(self):
        """Monitor network traffic in real-time."""
        print("Monitoring network traffic...")
        try:
            while True:
                net_io = psutil.net_io_counters()
                print(f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("Traffic monitoring stopped.")

if __name__ == "__main__":
    # Example usage
    monitor = TrafficMonitor(interval=2)
    monitor.monitor_traffic()
