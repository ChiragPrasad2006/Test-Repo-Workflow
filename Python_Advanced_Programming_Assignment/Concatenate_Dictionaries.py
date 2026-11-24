def concatenate_dictionaries(dicts: list[dict]) -> dict:
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result