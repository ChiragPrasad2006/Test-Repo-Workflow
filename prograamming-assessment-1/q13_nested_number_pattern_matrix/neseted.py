def generate_pattern_lines(rows):
    pattern = []
    for number in range(1, rows + 1):
        line = ""
        for count in range(number):
            line += str(number)
        pattern.append(line)
    return pattern
