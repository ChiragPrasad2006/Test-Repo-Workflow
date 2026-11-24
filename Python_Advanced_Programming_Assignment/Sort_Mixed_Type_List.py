def sort_mixed_list(lst: list) -> list:
    return sorted(lst, key=lambda item: (isinstance(item, str), item))
