import os
import json
from typing import Optional
from itertools import zip_longest
from rich.table import Table, Column
from rich.box import DOUBLE
from .settings import load_config
from .console import console
from .models import Task


class Board:
    def __init__(self):
        try:
            config = load_config()
        except FileNotFoundError:
            console.print(
                '[red]\[*][/] The config file does not exist, run "kanbanpy setup" to create it.')
            exit()

        try:
            with open(config['storage']) as storage:
                tasks_json = json.load(storage)
        except FileNotFoundError:
            console.print(
                f'[red]\[*][/] It seems the storage file does not exist.')
            console.print(
                f'[red]\[*][/] Please check that "{config["storage"]}" contains a valid JSON array.')
            exit()

        self.tasks = [Task(**t) for t in tasks_json]

    def add_task(self, task: Task):
        ...

    def move_task(self, task_id: int, *, reverse: bool = False):
        ...

    def delete_task(self, task_id: int):
        ...

    def clear_done(self):
        ...

    def show(self, message: Optional[str] = '[bright_white]Tip: run "kanbanpy -h" to show more commands.[/]'):
        cols = [
            Column('[bright_white]to do[/]', ratio=1,
                   no_wrap=True),
            Column('[bright_blue]in progress[/]', ratio=1, no_wrap=True),
            Column('[bright_green]done[/]', ratio=1, no_wrap=True)
        ]
        table = Table(*cols, expand=True, box=DOUBLE, caption_justify='full')

        todo = [str(t) for t in self.tasks if t.status == 'to do']
        inprogress = [str(t) for t in self.tasks if t.status == 'in progress']
        done = [str(t) for t in self.tasks if t.status == 'done']

        for row in zip_longest(todo, inprogress, done):
            table.add_row(*row)

        if message:
            table.caption = message

        console.print(table)
        print()
