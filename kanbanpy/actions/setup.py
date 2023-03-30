from typing import Any, Dict
from argparse import Namespace
from pathlib import Path
from ..settings import config_file, default_config, create_config, seed_data
from ..console import console


def handler(args: Namespace):
    """Handle creating the config file and data storage."""

    if Path(config_file).exists():
        console.print('[bright_red]\[*][/] Config file already exists.')
        return

    if args.defaults:
        create_config()

        # Create storage path and write the default data.
        if not Path(default_config['storage']).exists():
            Path(default_config['storage']).parent.mkdir(parents=True, exist_ok=True)
            seed_data(default_config['storage'])

        console.print(
            '[bright_green]\[+][/] Created config file using defaults.')
        return

    config: Dict[str, Any] = {}

    config['storage'] = input(
        f'Enter storage location (default: "{default_config["storage"]}"): ') or default_config['storage']

    config['wip_limit'] = int(input(
        f'Enter WIP limit (default: "{default_config["wip_limit"]}"): ') or default_config['wip_limit'])

    config['clear_screen'] = input('Clear screen before showing the board (y/N)? ').lower() in ('y', 'yes', 'true')

    create_config(config)

    # Create storage path and write user-provided data.
    if not Path(config['storage']).exists():
        Path(config['storage']).parent.mkdir(parents=True, exist_ok=True)
        seed_data(config['storage'])

    console.print('[bright_green]\[+][/] Created config file successfully.')
