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

    @classmethod
    def from_json(cls, obj: str):
        values = json.loads(obj)

        if any((key not in ('id', 'title', 'status')) for key in values.keys()):
            raise ValueError('Invalid key found in json object.')

        return cls(**values)

    def to_json(self):
        return json.dumps(self.__dict__)
