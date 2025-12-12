import pytest
from src.kanban_backend.task_rules import move_task

def test_valid_move():
    assert move_task("todo", "done", ["todo", "done"]) == "done"

def test_invalid_move():
    with pytest.raises(ValueError):
        move_task("todo", "archive", ["todo", "done"])
