import json

class Task:
    def __init__(self, id: int, title: str, status: str):
        self.id = id
        self.title = title
        self.status = status

    def __str__(self) -> str:
        return f'[{self.id}] {self.title}'

    def __repr__(self) -> str:
        return f'Task(id={self.id!r}, title={self.title!r}, status={self.status!r})'
