def find_matching_pairs(x: dict, y: dict) -> list[str]:
    result = []
    for key in x:
        if key in y and x[key] == y[key]:
            result.append(f"{key}: {x[key]} is present in both x and y")
    return result
