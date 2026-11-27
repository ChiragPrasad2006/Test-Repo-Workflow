def normalize_coordinates(coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
    smallest_x = min(x for x, y in coordinates)
    smallest_y = min(y for x, y in coordinates)
    result = []
    for x, y in coordinates:
        result.append((x - smallest_x, y - smallest_y))
    return result
