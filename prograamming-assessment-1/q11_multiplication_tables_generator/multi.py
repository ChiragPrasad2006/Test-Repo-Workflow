def generate_tables(targets, limit):
    tables = {}
    for target in targets:
        table = []
        for multiplier in range(1, limit + 1):
            table.append(target * multiplier)
        tables[target] = table
    return tables
