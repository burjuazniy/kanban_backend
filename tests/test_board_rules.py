import pytest
from src.kanban_backend.board_rules import next_column

def test_next_column_ok():
    cols = ["todo", "in_progress", "done"]
    assert next_column(cols, "todo") == "in_progress"

def test_last_column_error():
    with pytest.raises(ValueError):
        next_column(["todo", "done"], "done")
