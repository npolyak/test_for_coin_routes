def to_float(str_value: str, default: float = -1.) -> float:
    try:
        return float(str_value)
    except (ValueError, TypeError):
        return None
