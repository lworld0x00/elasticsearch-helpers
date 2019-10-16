import os
from os.path import dirname
from configparser import ConfigParser

PROJECT_ROOT_DIR = dirname(dirname(__file__))
# print(PROJECT_ROOT_DIR)
CONFIG_FILE = os.path.join(PROJECT_ROOT_DIR, "Conf/config.ini")


def get_config(section, option):
    config_parser = ConfigParser()
    config_parser.read(CONFIG_FILE)
    option = config_parser.get(section, option)

    return option




