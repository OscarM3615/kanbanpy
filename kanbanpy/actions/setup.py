from typing import Any, Dict
from argparse import Namespace
from pathlib import Path
from ..settings import default_config, create_config, seed_data
from ..console import console


def handler(args: Namespace):
    """Handle creating the config file and data storage."""

    if args.defaults:
        create_config()
        Path(default_config['storage']).parent.mkdir(parents=True, exist_ok=True)
        seed_data(default_config['storage'])

        console.print(
            '[bright_green]\[+] Created config file using defaults.[/]')
        return

    config: Dict[str, Any] = {}
    config['storage'] = input(
        f'Enter storage location (default: "{default_config["storage"]}"): ') or default_config['storage']
    config['wip_limit'] = int(input(
        f'Enter WIP limit (default: "{default_config["wip_limit"]}"): ') or default_config['wip_limit'])

    create_config(config)
    Path(config['storage']).parent.mkdir(parents=True, exist_ok=True)
    seed_data(config['storage'])

    console.print('[bright_green]\[+] Created config file successfully.[/]')
