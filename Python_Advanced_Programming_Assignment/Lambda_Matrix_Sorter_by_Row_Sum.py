def sort_matrix_by_row_sum(matrix: list[list[int]]) -> list[list[int]]:
    return sorted(matrix, key=lambda row: sum(row))
