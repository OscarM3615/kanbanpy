"""
A console-based Kanban task manager created in Python.

This module parses the command line arguments and call the respective handler.
"""

from .cli import parser
from .actions import clear, create, default, next_, prev, remove, setup


handlers = {
    'create': create.handler,
    'c': create.handler,
    'next': next_.handler,
    'n': next_.handler,
    'prev': prev.handler,
    'p': prev.handler,
    'remove': remove.handler,
    'r': remove.handler,
    'clear': clear.handler,
    'setup': setup.handler
}


def main():
    """Parse console arguments and call the required parser. The help argument is handled automatically."""

    args = parser.parse_args()
    handler = handlers.get(args.command, default.handler)
    handler(args)


if __name__ == '__main__':
    main()
