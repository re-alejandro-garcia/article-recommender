# Load/Save app information from/to a .yaml file given a file location.
# All methods accept an optional logger for logging error messages.

# TO DO: change sys.exit() line in the error handling code for both functions.

import yaml
import os
import io
import traceback
import sys
import logging


class Save_File_IO:
    @staticmethod
    def load_website_info(save_file_path: str, logger: logging.Logger = None) -> dict:
        try:
            website_info = dict()
            with open(save_file_path, "rt") as f:
                website_info = yaml.safe_load(f.read())
            return website_info
        except FileNotFoundError as fe:
            if logger:
                logger.error(
                    "FileNotFoundError occurred in Save_File_IO.py load_website_info()."
                )
                logger.error(f"\nFile {save_file_path} not found.")
                logger.error(
                    "From Save_File_IO.py verify that parameter save_file_path is correct.\n"
                )
            else:
                traceback.print_exc()
                print(f"\nFile {save_file_path} not found.")
                print(
                    "From Save_File_IO.py verify that parameter save_file_path is correct.\n"
                )
            sys.exit()

    @staticmethod
    def save_website_info(
        save_file_path: str, website_info_dict: dict, logger: logging.Logger = None
    ):
        try:
            with io.open(save_file_path, "w", encoding="utf8") as outfile:
                yaml.dump(
                    website_info_dict,
                    outfile,
                    default_flow_style=False,
                    allow_unicode=True,
                )
        except FileNotFoundError as fe:
            if logger:
                logger.error(
                    "FileNotFoundError occurred in Save_File_IO.py save_website_info()."
                )
                logger.error(f"\nFile {save_file_path} not found.")
                logger.error(
                    "From Save_File_IO.py verify that parameter save_file_path is correct.\n"
                )
            else:
                traceback.print_exc()
                print(f"\nFile {save_file_path} not found.")
                print(
                    "From Save_File_IO.py verify that parameter save_file_path is correct.\n"
                )
            sys.exit()
