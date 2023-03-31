"""
This module defines all the command line interface arguments that can be used to call the CLI.
"""

from argparse import ArgumentParser


parser = ArgumentParser(
    prog='kanbanpy', description='Console-based kanban task manager')
subparsers = parser.add_subparsers(dest='command')

create_parser = subparsers.add_parser(
    'create', help='create a new task', description='Create a new task', aliases=['c'])
create_parser.add_argument('title', type=str, help='task title')

next_parser = subparsers.add_parser(
    'next', help='move a task to the next status', description='Move a task to the next status', aliases=['n'])
next_parser.add_argument('id', type=int, help='task id')

prev_parser = subparsers.add_parser('prev', help='move a task to the previous status',
                                    description='Move a task to the previous status', aliases=['p'])
prev_parser.add_argument('id', type=int, help='task id')

remove_parser = subparsers.add_parser(
    'remove', help='remove a task', description='Remove a task', aliases=['r'])
remove_parser.add_argument('id', type=int, help='task id')

clear_parser = subparsers.add_parser(
    'clear', help='remove all completed tasks', description='Remove all completed tasks')

setup_parser = subparsers.add_parser(
    'setup', help='create the configuration file', description='Create the configuration file')
setup_parser.add_argument('-y', dest='defaults',
                          action='store_true', help='use defaults')

backup_parser = subparsers.add_parser(
    'backup', help='create a backup file', description='Create a backup file')
backup_parser.add_argument(
    '-o', dest='output', type=str, help='destination file')
