from src.kanban_backend.history import create_history_event

def test_history_event_structure():
    event = create_history_event("u1", "move", {"a": 1}, {"a": 2})
    assert event["user_id"] == "u1"
    assert event["action"] == "move"
