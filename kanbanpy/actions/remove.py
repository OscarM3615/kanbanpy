from argparse import Namespace
from ..board import Board

def handler(args: Namespace):
    """Handle removing a task and display the board."""

    board = Board()
    try:
        board.delete_task(args.id)
        board.show('[bright_green]Deleted task successfully.[/]')
    except ValueError:
        board.show(f'[bright_red]Unable to find task with id {args.id}.[/]')
