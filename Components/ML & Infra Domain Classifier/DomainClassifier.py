import yaml
import sys

class DomainClassifier:
    def __init__(self, config):
        self.tags = config.get('tags', [])

    def classify(self, resource):
        """
        Classify a resource based on tags.
        """
        domain = "unknown"
        for tag in self.tags:
            if tag in resource.get('tags', []):
                domain = self.tags[tag]
                break
        return domain

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
    classifier = DomainClassifier(config)

    # Example resource (would normally be sourced from Azure ML or Terraform)
    resource = {"name": "example_resource", "tags": ["ml"]}

    domain = classifier.classify(resource)
    print(f"Resource '{resource['name']}' classified into domain: {domain}")

if __name__ == "__main__":
    config_file = "ClassifierConfig.yaml" if len(sys.argv) < 2 else sys.argv[1]
    main(config_file)
