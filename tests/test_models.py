from typing import Callable

import pytest

from kanbanpy.models import Board, Status, Task


@pytest.fixture
def task():
    """Generate a default state task.
:return: task
    """
    return Task('my new todo', Status.TO_DO)


@pytest.fixture
def make_task():
    """Generate a task with specific.
    """
    def _make_task(status: Status):
        return Task('my new todo', status)

    return _make_task


@pytest.fixture
def board():
    """Generate an empty board.

    :return: board
    """
    return Board([])


class TestTask:
    def test_str_method(self, task: Task):
        """Test that converting the task to string will contain the title and
        id.
        """
        converted = str(task)

        assert task.title in converted
        assert str(task.id) in converted

    def test_rich_method(self, task: Task):
        """Test that the renderable will contain the task title and id.
        """
        # rich module will call this method automatically
        converted = task.__rich__()

        assert task.title in converted
        assert str(task.id) in converted

    def test_json_structure(self, task: Task):
        """Test that the JSON structure contains all important fields.
        """
        json_dict = task.to_json()

        assert json_dict['id'] == task.id
        assert json_dict['title'] == task.title
        assert json_dict['status'] == task.status

    def test_move_valid(self, task: Task):
        """Test that moving the task updates the status.
        """
        task.move_to('right')
        assert task.status == Status.IN_PROGRESS

        task.move_to('left')
        assert task.status == Status.TO_DO

    def test_move_invalid(self, task: Task):
        """Test that trying to move to an non existing status raises an error.
        """
        with pytest.raises(ValueError):
            task.move_to('left')


class TestBoard:
    def test_json_structure(self, board: Board, task: Task):
        """Test that the JSON structure contains all important fields.
        """
        board.add(task)
        json_obj = board.to_json()

        assert isinstance(json_obj, list)
        assert isinstance(json_obj[0], dict)
        assert json_obj[0]['title'] == task.title

    def test_add_task(self, board: Board, task: Task):
        """Test that the task is added to the board.
        """
        board.add(task)
        assert len(board) == 1
        assert task in board

    def test_remove_task(self, board: Board, task: Task):
        """Test that the task is removed from the board.
        """
        board.add(task)
        assert task in board
        board.remove(task.id)
        assert task not in board

    def test_move_task(self, board: Board, make_task: Callable[[Status], Task]):
        """Test that the task status is updated after moving.
        """
        task = make_task(Status.IN_PROGRESS)
        board.add(task)
        board.move(task.id, 'right')

        assert task.status == Status.REVIEW

    def test_clear_done(self, make_task: Callable[[Status], Task]):
        """Test that the board removes all done tasks.
        """
        todo_task = make_task(Status.TO_DO)
        review_task = make_task(Status.REVIEW)
        done_task = make_task(Status.DONE)

        board = Board([todo_task, review_task, done_task])
        board.remove_done()

        assert len(board) == 2
        assert done_task not in board
