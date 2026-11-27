def square_index_map(n: int) -> dict[int, int]:
    result = {}
    for number in range(1, n + 1):
        result[number] = number * number
    return result
