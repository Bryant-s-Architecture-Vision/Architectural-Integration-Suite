# SQLConnector.py
import argparse
import json
import sqlite3

def connect_to_database(config_path):
    # Load configuration data
    with open(config_path, 'r') as file:
        config = json.load(file)

    # Connect to the SQL database
    connection = sqlite3.connect(config['database_path'])
    cursor = connection.cursor()

    # Placeholder for database query logic
    # Example: Fetching data for frontend display
    cursor.execute("SELECT * FROM Architecture")
    data = cursor.fetchall()

    # Logic to interface with React components (can be adjusted as needed)
    print("Data fetched for frontend display:", data)

    # Close the connection
    connection.close()

def main(config_path):
    connect_to_database(config_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, required=True)

    args = parser.parse_args()
    main(args.config_path)
