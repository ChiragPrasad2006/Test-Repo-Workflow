def calculate_total_cost(quantity):
    total = quantity * 100
    if total > 1000:
        total = total * 0.9
    return total
