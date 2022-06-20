import yaml
import logging
from logging import config
import traceback
import sys
import os

config_yaml_file_location = os.path.join(os.path.dirname(__file__), "Config.yaml")


def configure_logger():
    try:
        with open(config_yaml_file_location, "rt") as f:
            config_data = yaml.safe_load(f.read())
            logging.config.dictConfig(config_data)
    except FileNotFoundError as fe:
        traceback.print_exc()
        print(f"\nFile {config_yaml_file_location} not found.")
        print(
            "In configure_logger.py check that file location for config.yaml is correct.\n"
        )
        sys.exit()
