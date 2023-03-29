from argparse import Namespace
from ..board import Board

def handler(args: Namespace):
    """Handle moving a task to the previous status and display the board."""

    board = Board()
    try:
        board.move_task(args.id, reverse=True)
        board.show(f'[bright_green]Moved task with id {args.id}.[/]')
    except ValueError as ex:
        board.show(f'[bright_red]{ex}[/]')
    except IndexError:
        board.show('[bright_red]Task is already in the first status.[/]')
