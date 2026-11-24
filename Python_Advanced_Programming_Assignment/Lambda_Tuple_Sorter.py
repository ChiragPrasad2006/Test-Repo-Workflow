def sort_tuples_by_value(tuples_list: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(tuples_list, key=lambda item: item[1])
