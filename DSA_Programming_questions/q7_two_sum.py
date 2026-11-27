def two_sum(numbers: list[int], target: int) -> list[int]:
    seen = {}
    for index, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return [seen[needed], index]
        seen[number] = index
    return []
