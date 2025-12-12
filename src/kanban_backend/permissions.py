def can_edit_task(role: str) -> bool:
    return role in ("owner", "member")
