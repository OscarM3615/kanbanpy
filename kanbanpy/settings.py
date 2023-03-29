"""
This module defines the static app settings, such as the app defaults or config file location.
"""

import os
import json
from typing import Any, Dict, List, Optional
from platformdirs import user_config_path
from .models import Task


config_file = os.path.join(os.path.expanduser('~'), '.kanbanpy.json')

default_config: Dict[str, Any] = {
    # ~/.config/kanbanpy/kanbanpy.json
    'storage': str(user_config_path().joinpath('kanbanpy').joinpath('kanbanpy.json')),
    'wip_limit': 5
}

default_data: List[Task] = []

statuses = ('to do', 'in progress', 'done')


def load_config() -> Dict[str, Any]:
    """Load the json config file into a dict."""
    with open(config_file) as conf:
        config = json.load(conf)
    return config


def create_config(config: Optional[Dict[str, Any]] = None):
    """Create a config file with the function arguments or the default config."""
    with open(config_file, 'w') as conf:
        if config:
            json.dump(config, conf)
        else:
            json.dump(default_config, conf)


def seed_data(path: str):
    """Create a data file in path with an empty list of tasks."""
    with open(path, 'w') as dat:
        json.dump(default_data, dat)
