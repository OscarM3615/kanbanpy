import re
from platformdirs import user_data_path
from rich import print

from kanbanpy.models import Board, Status, Task
from kanbanpy.storage import Storage
from .cli import parser


def main():
    args = parser.parse_args()
    command = args.command

    storage = Storage(user_data_path('kanbanpy') / 'tasks.json')
    tasks = [Task(item['title'], Status(item['status']), id=item['id'])
             for item in storage.read()]
    board = Board(tasks)

    if command is None:
        ...  # do nothing, just show the board
    elif re.match(r'^(c|create)$', command):
        task = Task(args.title)
        board.add(task)
        storage.write(board.to_json())
    elif re.match(r'^(n|next)$', command):
        try:
            board.move(args.id, 'right', args.steps)
            storage.write(board.to_json())
        except ValueError as err:
            print(rf'[red]\[*][/] {err}.')
    elif re.match(r'^(p|prev)$', command):
        try:
            board.move(args.id, 'left', args.steps)
            storage.write(board.to_json())
        except ValueError as err:
            print(rf'[red]\[*][/] {err}.')
    elif re.match(r'^(r|remove)$', command):
        try:
            board.remove(args.id)
            storage.write(board.to_json())
        except ValueError as err:
            print(rf'[red]\[*][/] {err}.')
    elif re.match(r'^(m|rename)$', command):
        try:
            board.rename(args.id, args.title)
        except ValueError as err:
            print(rf'[red]\[*][/] {err}.')
    elif command == 'clear':
        board.remove_done()
        storage.write(board.to_json())

    print(board)


if __name__ == '__main__':
    main()
