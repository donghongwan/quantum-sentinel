import os

class LogAggregation:
    """Aggregation of logs from multiple sources."""
    
    def __init__(self, log_sources, output_file):
        self.log_sources = log_sources
        self.output_file = output_file

    def aggregate_logs(self):
        """Aggregate logs from multiple sources into a single file."""
        with open(self.output_file, 'w') as outfile:
            for log_source in self.log_sources:
                with open(log_source, 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")  # Add a newline between logs

if __name__ == "__main__":
    # Example usage
    log_sources = ['logs/app.log', 'logs/system.log']
    log_aggregation = LogAggregation(log_sources, 'logs/aggregated_logs.log')
    log_aggregation.aggregate_logs()
    print("Logs aggregated into:", log_aggregation.output_file)
