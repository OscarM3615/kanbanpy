"""
This module defines the static app settings, such as the app defaults or config file location.
"""

import os
import json
from typing import Dict, List
from platformdirs import user_config_path
from .models import Task


config_file = os.path.join(os.path.expanduser('~'), '.kanbanpy.json')

default_config = {
    # ~/.config/kanbanpy/kanbanpy.json
    'storage': str(user_config_path().joinpath('kanbanpy').joinpath('kanbanpy.json')),
    'wip_limit': 5
}

default_data: List[Task] = []


def load_config():
    with open(config_file) as conf:
        config = json.load(conf)
    return config


def create_config():
    with open(config_file, 'w') as conf:
        json.dump(default_config, conf)


def seed_data(path: str):
    with open(path, 'w') as dat:
        json.dump(default_data, dat)
