def filter_tasks(tasks: list[dict], tag: str | None = None):
    if tag is None:
        return tasks
    return [t for t in tasks if tag in t["tags"]]
