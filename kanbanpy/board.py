import os
import json
from typing import Optional
from itertools import zip_longest
from rich.table import Table, Column
from rich.box import DOUBLE
from .settings import load_config, statuses
from .console import console
from .models import Task


class Board:
    def __init__(self):
        try:
            self.config = load_config()
        except FileNotFoundError:
            console.print(
                '[red]\[*][/] The config file does not exist, run "kanbanpy setup" to create it.')
            exit()

        try:
            with open(self.config['storage']) as storage:
                tasks_json = json.load(storage)
        except FileNotFoundError:
            console.print(
                f'[bright_red]\[*][/] It seems the storage file does not exist.')
            console.print(
                f'[bright_red]\[*][/] Please check that "{self.config["storage"]}" contains a valid JSON array.')
            exit()

        self.tasks = [Task(**t) for t in tasks_json]

    def _save_json(self):
        with open(self.config['storage'], 'w') as data:
            json.dump([t.json() for t in self.tasks], data)

    def add_task(self, task: Task):
        next_id = 1
        if len(self.tasks):
            next_id += self.tasks[-1].id

        task.id = next_id
        self.tasks.append(task)

        self._save_json()


    def move_task(self, task_id: int, *, reverse: bool = False):
        try:
            task = [t for t in self.tasks if t.id == task_id][0]
        except IndexError:
            raise ValueError(f'Unable to find task with id {task_id}.')

        if not reverse:
            if task.status == 'done':
                raise IndexError('task is already in last status')
            task.status = statuses[statuses.index(task.status) + 1]
        else:
            if task.status == 'to do':
                raise IndexError('task is already in first status')
            task.status = statuses[statuses.index(task.status) - 1]

        wip = [t for t in self.tasks if t.status == 'in progress']
        if len(wip) > self.config['wip_limit']:
            task.status = 'to do' if not reverse else 'done'
            raise ValueError(f'Can not exceed the WIP limit ({self.config["wip_limit"]}).')

        self._save_json()

    def delete_task(self, task_id: int):
        new_tasks = [t for t in self.tasks if t.id != task_id]

        if len(new_tasks) == len(self.tasks):
            raise ValueError(f'task with id {task_id} not found')

        self.tasks = new_tasks
        self._save_json()

    def clear_done(self):
        self.tasks = [t for t in self.tasks if t.status != 'done']
        self._save_json()

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

        if self.config['clear_screen']:
            os.system('cls' if os.name == 'nt' else 'clear')

        console.print(table)
        print()
