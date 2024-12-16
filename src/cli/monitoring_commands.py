import psutil

class MonitoringCommands:
    def check_cpu_usage(self):
        """Check and print CPU usage."""
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")

    def check_memory_usage(self):
        """Check and print memory usage."""
        memory = psutil.virtual_memory()
        print(f"Memory Usage: {memory.percent}% used of {memory.total / (1024 ** 2):.2f} MB")

    def check_disk_usage(self):
        """Check and print disk usage."""
        disk = psutil.disk_usage('/')
        print(f"Disk Usage: {disk.percent}% used of {disk.total / (1024 ** 3):.2f} GB")

if __name__ == "__main__":
    # Example usage
    monitoring_commands = MonitoringCommands()
    monitoring_commands.check_cpu_usage()
    monitoring_commands.check_memory_usage()
    monitoring_commands.check_disk_usage()
