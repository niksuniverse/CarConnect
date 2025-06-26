
import os

def get_db_config(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # current script's dir
    file_path = os.path.join(base_dir, file_name)
    config = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config
