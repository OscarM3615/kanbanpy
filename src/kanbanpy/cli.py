from argparse import ArgumentParser
from . import __version__


parser = ArgumentParser(
    'kanbanpy',
    description='Console-based kanban task manager'
)
parser.add_argument(
    '-v', '--version',
    action='version',
    version=f'%(prog)s v{__version__}'
)

subparsers = parser.add_subparsers(dest='command')

create_parser = subparsers.add_parser(
    'create',
    help='create new task',
    description='Add a new task to the board',
    aliases=('c',)
)
create_parser.add_argument('title', type=str, help='task title')

next_parser = subparsers.add_parser(
    'next',
    help='move to next status',
    description='Move a task to the next status in the board',
    aliases=('n',)
)
next_parser.add_argument('id', type=int, help='task id')

prev_parser = subparsers.add_parser(
    'prev',
    help='move to previous status',
    description='Move a task to the previous status in the board',
    aliases=('p',)
)
prev_parser.add_argument('id', type=int, help='task id')

remove_parser = subparsers.add_parser(
    'remove',
    help='remove task',
    description='Delete a task from the board',
    aliases=('r',)
)
remove_parser.add_argument('id', type=int, help='task id')

clear_parser = subparsers.add_parser(
    'clear',
    help='clear done tasks',
    description='Remove all done tasks from the board'
)
