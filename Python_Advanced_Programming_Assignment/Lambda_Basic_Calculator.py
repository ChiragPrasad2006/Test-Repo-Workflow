def evaluate_lambda_ops(num: int, x: int, y: int) -> tuple[int, int]:
    add_fifteen = lambda number: number + 15
    multiply = lambda first, second: first * second
    return add_fifteen(num), multiply(x, y)
