def partition_numbers(n: int) -> dict[str, list[int]]:
    result = {"even": [], "odd": [], "prime": []}
    for number in range(1, n + 1):
        is_prime = number > 1
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            result["prime"].append(number)
        elif number % 2 == 0:
            result["even"].append(number)
        else:
            result["odd"].append(number)
    return result
