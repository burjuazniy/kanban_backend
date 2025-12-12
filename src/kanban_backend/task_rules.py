def move_task(current: str, target: str, allowed: list[str]) -> str:
    if target not in allowed:
        raise ValueError("Invalid column")
    return target
