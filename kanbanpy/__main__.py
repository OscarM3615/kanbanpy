"""
A console-based Kanban task manager created in Python.

This module parses the command line arguments and call the respective handler.
"""

from .cli import parser as default_parser
from .actions import clear, create, next_, prev, remove


handlers = {
    'create': create.handler,
    'next': next_.handler,
    'prev': prev.handler,
    'remove': remove.handler,
    'clear': clear.handler
}


def default_help(*args):
    """Print the global CLI help."""
    default_parser.print_help()

def main():
    """Parse console arguments and call the required parser."""
    args = default_parser.parse_args()

    handler = handlers.get(args.command, default_help)
    handler(args)

if __name__ == '__main__':
    main()
