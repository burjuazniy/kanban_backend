def create_history_event(user_id: str, action: str, before: dict, after: dict) -> dict:
    return {
        "user_id": user_id,
        "action": action,
        "before": before,
        "after": after,
    }
