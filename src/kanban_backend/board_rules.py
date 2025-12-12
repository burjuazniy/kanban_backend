def next_column(columns: list[str], current: str) -> str:
    idx = columns.index(current)
    if idx == len(columns) - 1:
        raise ValueError("Already last column")
    return columns[idx + 1]
