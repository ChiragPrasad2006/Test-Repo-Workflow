def highest_three_values(d: dict[str, int]) -> list[int]:
    values = sorted(d.values(), reverse=True)
    return values[:3]
