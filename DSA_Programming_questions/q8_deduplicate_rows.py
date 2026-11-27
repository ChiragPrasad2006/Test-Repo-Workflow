def deduplicate_rows(matrix: list[list[int]]) -> list[list[int]]:
    seen = set()
    result = []
    for row in matrix:
        row_key = tuple(row)
        if row_key not in seen:
            seen.add(row_key)
            result.append(row)
    return result
