def are_all_dicts_empty(lst: list[dict]) -> bool:
    return all(not dictionary for dictionary in lst)
