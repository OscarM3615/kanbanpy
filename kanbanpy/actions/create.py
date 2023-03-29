from argparse import Namespace
from ..models import Task
from ..board import Board

def handler(args: Namespace):
    """Handle task creation and display the board."""

    task = Task(0, args.title, 'to do')
    board = Board()
    board.add_task(task)
    board.show('[bright_green]Created new task.[/]')
