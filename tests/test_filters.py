from src.kanban_backend.filters import filter_tasks

def test_filter_by_tag():
    tasks = [
        {"id": 1, "tags": ["bug"]},
        {"id": 2, "tags": ["feature"]},
    ]
    result = filter_tasks(tasks, "bug")
    assert len(result) == 1
