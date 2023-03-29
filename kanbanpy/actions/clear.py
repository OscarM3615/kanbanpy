from argparse import Namespace
from ..board import Board

def handler(args: Namespace):
    """Handle clearing all done tasks and display the board."""

    board = Board()
    board.clear_done()
    board.show('[bright_green]Cleared all done tasks.[/]')
