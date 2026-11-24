def merge_and_sum_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
