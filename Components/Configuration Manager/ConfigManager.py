# ConfigManager.py
import json
import argparse

def load_configuration(config_path):
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

def save_configuration(config_path, config):
    with open(config_path, 'w') as file:
        json.dump(config, file, indent=4)

def update_configuration(config_path, new_settings):
    config = load_configuration(config_path)
    config.update(new_settings)
    save_configuration(config_path, config)

def main(config_path, new_settings_path):
    new_settings = load_configuration(new_settings_path)
    update_configuration(config_path, new_settings)
    print("Configuration updated successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, required=True)
    parser.add_argument('--new_settings_path', type=str, required=True)

    args = parser.parse_args()
    main(args.config_path, args.new_settings_path)
