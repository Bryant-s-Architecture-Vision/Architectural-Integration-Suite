import yaml
import uuid
import sys

class UIDGenerator:
    def __init__(self, config):
        self.prefix = config.get('prefix', 'UID')
        self.counter = config.get('initial_count', 1000)

    def generate_uid(self):
        """
        Generate a unique identifier.
        Uses a UUID if specified, otherwise uses an incrementing counter.
        """
        if config.get('use_uuid'):
            return f"{self.prefix}-{uuid.uuid4()}"
        else:
            self.counter += 1
            return f"{self.prefix}-{self.counter}"

def load_config(config_path):
    """
    Load configuration from a YAML file.
    """
    try:
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Configuration file {config_path} not found. Using default settings.")
        return {}

def main(config_file):
    config = load_config(config_file)
    uid_gen = UIDGenerator(config)
    uid = uid_gen.generate_uid()
    print(f"Generated UID: {uid}")

if __name__ == "__main__":
    config_file = "UIDGenConfig.yaml" if len(sys.argv) < 2 else sys.argv[1]
    main(config_file)
