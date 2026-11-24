def extend_list_without_append(list1: list, list2: list) -> list:
    result = list1[:]
    result.extend(list2)
    return result
