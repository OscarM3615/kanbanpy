from ..board import Board
from ..settings import app_version

def handler(args):
    """Display the board."""

    if args.version:
        print(f'kanbanpy {app_version}')
        return

    board = Board()
    board.show()
