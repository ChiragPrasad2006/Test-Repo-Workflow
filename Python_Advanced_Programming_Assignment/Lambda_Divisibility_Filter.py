def filter_divisibles(nums: list[int]) -> list[int]:
    is_divisible = lambda number: number % 19 == 0 or number % 13 == 0
    return list(filter(is_divisible, nums))
