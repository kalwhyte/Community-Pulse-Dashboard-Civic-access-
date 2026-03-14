def normalize_score(value: float, min_value: float, max_value: float) -> float:
    """
    Normalize a value to the 0..1 range.
    """
    if max_value == min_value:
        return 0.0
    return (value - min_value) / (max_value - min_value)


def calculate_mismatch(social_score: float, official_score: float) -> float:
    """
    Compute the absolute difference between two scores.
    """
    return round(abs(social_score - official_score), 3)