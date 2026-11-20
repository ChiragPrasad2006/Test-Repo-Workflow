def insert_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    return dictionary
