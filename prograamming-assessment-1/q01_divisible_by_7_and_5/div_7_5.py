def find_divisibles(low, high):
    numbers = []
    for number in range(low, high + 1):
        if number % 7 == 0 and number % 5 == 0:
            numbers.append(number)
    return numbers
