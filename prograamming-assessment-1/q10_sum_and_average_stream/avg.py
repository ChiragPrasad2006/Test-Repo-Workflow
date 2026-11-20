def process_stream(inputs):
    total = 0
    count = 0

    for number in inputs:
        if number == 0:
            break
        total += number
        count += 1

    if count == 0:
        return 0, 0.0
    return total, total / count
