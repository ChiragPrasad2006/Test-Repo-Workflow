def classify_triangle(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return "Invalid"
    if x + y <= z or x + z <= y or y + z <= x:
        return "Invalid"
    if x == y == z:
        return "Equilateral"
    if x == y or x == z or y == z:
        return "Isosceles"
    return "Scalene"
