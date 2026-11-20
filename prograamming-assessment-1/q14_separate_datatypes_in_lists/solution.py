def segregate_datatypes(mixed_list):
    integers = []
    strings = []
    floats = []

    for value in mixed_list:
        if type(value) is int:
            integers.append(value)
        elif type(value) is str:
            strings.append(value)
        elif type(value) is float:
            floats.append(value)

    integers.sort()
    strings.sort()
    floats.sort()
    return integers, strings, floats
