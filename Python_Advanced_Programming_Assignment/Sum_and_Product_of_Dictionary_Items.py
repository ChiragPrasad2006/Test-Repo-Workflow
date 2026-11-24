def sum_and_multiply_values(d: dict[str, int]) -> tuple[int, int]:
    total = 0
    product = 1
    for value in d.values():
        total += value
        product *= value
    return total, product
