"""This module contains the classes used to represent the application data and
its behaviour.
"""


from collections import defaultdict
from collections.abc import Iterable, Mapping
from enum import IntEnum
from typing import Literal, Optional

from rich.box import DOUBLE_EDGE
from rich.console import Group
from rich.table import Table, Column


class Status(IntEnum):
    """This enum represents each status of the Kanban board.
    """
    TO_DO = 1
    IN_PROGRESS = 2
    REVIEW = 3
    DONE = 4


class Task:
    """This class encapsulates the behaviour of a task and the JSON
    representation.
    """

    def __init__(self, title: str, status: Status = Status.TO_DO, id: Optional[int] = None):
        """Initialise a task.

        :param title: task title
        :param status: task status, defaults to Status.TO_DO
        :param id: explicitly set id, defaults to None
        """
        self.id = id or 0  # if 0 it will be overriden when adding to a board
        self.title = title
        self.status = status

    def __str__(self) -> str:
        """Generate the plain task format.

        :return: task as plain string
        """
        return f'[{self.id}] {self.title}'

    def __repr__(self) -> str:
        """Generate the string format for debugging.

        :return: task as string
        """
        return f'Task(id={self.id!r}, title={self.title!r}, status={self.status.name})'

    def __rich__(self) -> str:
        """Generate the renderable format of a task to insert in the Kanban
        board.

        :return: renderable task
        """
        if '!' in self.title:
            return rf'[yellow]\[[cyan]{self.id}[/]] {self.title}[/]'
        return rf'\[[cyan]{self.id}[/]] {self.title}'

    def to_json(self) -> Mapping:
        """Generate the JSON representation of the task.

        :return: JSON mapping
        """
        return {'id': self.id, 'title': self.title, 'status': self.status}

    def move_to(self, direction: Literal['right', 'left'], steps: int):
        """Update the task status.

        :param direction: direction in the board to move the task
        :param steps: amount of steps to move
        :raises ValueError: if trying to move the task outside the status bounds
        """
        move_to = steps if direction == 'right' else steps * -1

        try:
            self.status = Status(self.status + move_to)
        except ValueError:
            # this changes the message to be shown
            raise ValueError('Unable to move the task')


class Board:
    """This class acts as a container for the tasks and handles the creation of
    a renderable object.
    """

    def __init__(self, tasks: list[Task]):
        """Initialise the board.

        :param tasks: list of tasks to add
        """
        self._tasks = tasks

    def __repr__(self) -> str:
        """Generate the string format of the board for debugging.

        :return: board as string
        """
        return f'Board(task_count={len(self)})'

    def __len__(self) -> int:
        """Calculate the total amount of tasks

        :return: total amount of tasks
        """
        return len(self._tasks)

    def __contains__(self, other: Task) -> bool:
        """Define if a task is included in the board.

        :param other: task object
        :return: if its contained or not
        """
        return other in self._tasks

    def __rich__(self) -> Table:
        """Generate the renderable object for rich module.

        :return: Table object
        """
        statuses: defaultdict[Status, list[Task]] = defaultdict(list)
        for task in self._tasks:
            statuses[task.status].append(task)

        table = Table(
            Column(
                f'[bright_white]to do[/] ({len(statuses[Status.TO_DO])})',
                ratio=1
            ),
            Column(
                f'[bright_blue]in progress[/] ({len(statuses[Status.IN_PROGRESS])})',
                ratio=1
            ),
            Column(
                f'[bright_magenta]review[/] ({len(statuses[Status.REVIEW])})',
                ratio=1
            ),
            Column(
                f'[bright_green]done[/] ({len(statuses[Status.DONE])})',
                ratio=1
            ),
            box=DOUBLE_EDGE,
            expand=True
        )

        table.add_row(
            Group(*statuses[Status.TO_DO]),
            Group(*statuses[Status.IN_PROGRESS]),
            Group(*statuses[Status.REVIEW]),
            Group(*statuses[Status.DONE])
        )

        return table

    def to_json(self) -> Iterable:
        """Generate the JSON representation of the board.

        :return: JSON list
        """
        return [t.to_json() for t in self._tasks]

    def add(self, task: Task):
        """Add a task to the board.

        :param task: task object
        """
        new_id = self._tasks[-1].id + 1 if len(self._tasks) else 1
        task.id = new_id

        self._tasks.append(task)

    def remove(self, task_id: int):
        """Remove a task from the board.

        :param task_id: task id
        :raises ValueError: if the task id is not found
        """
        task = next((t for t in self._tasks if t.id == task_id), None)
        if not task:
            raise ValueError('The task was not found')

        self._tasks.remove(task)

    def remove_done(self):
        """Remove all tasks with done status.
        """
        self._tasks = [t for t in self._tasks if t.status != Status.DONE]

    def move(self, task_id: int, direction: Literal['left', 'right'],
             steps: int):
        """Update a task's status by providing a direction.

        :param task_id: task id
        :param direction: direction to move in the board
        :param steps: amount of steps to move
        :raises ValueError: if the task id is not found
        """
        task = next((t for t in self._tasks if t.id == task_id), None)
        if not task:
            raise ValueError('The task was not found')

        task.move_to(direction, steps)

    def rename(self, task_id: int, title: str):
        """Update the title of a task.

        :param task_id: task id
        :param title: new task title
        :raises ValueError: if the task id is not found
        """
        task = next((t for t in self._tasks if t.id == task_id), None)
        if not task:
            raise ValueError('The task was not found')

        task.title = title
