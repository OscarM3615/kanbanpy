import os
import shutil
from argparse import Namespace
from pathlib import Path
from datetime import datetime
from ..console import console
from ..settings import load_config

def handler(args: Namespace):
    """Create a backup file in the path provided or in the config folder."""

    config = load_config()

    data_file = Path(config['storage'])
    data_name = data_file.name
    data_location = data_file.parent

    now = datetime.now().strftime(r'%Y_%m_%d_%H_%M_%S')
    dest_file = args.output or data_location.joinpath(f'{now}_{data_name}.bak')

    shutil.copyfile(config['storage'], dest_file)
    console.print(f'[green]\[+][/] Created backup to "{dest_file}".')
