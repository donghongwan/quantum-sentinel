import json

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        """Load configuration from a JSON file."""
        with open(self.config_file, 'r') as file:
            self.config = json.load(file)

    def get(self, key):
        """Get a configuration value by key."""
        return self.config.get(key, None)

if __name__ == "__main__":
    # Example usage
    config_manager = ConfigManager("config.json")
    print("Data file:", config_manager.get("data_file"))
