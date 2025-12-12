from src.kanban_backend.permissions import can_edit_task

def test_owner_can_edit():
    assert can_edit_task("owner") is True

def test_observer_cannot_edit():
    assert can_edit_task("observer") is False
