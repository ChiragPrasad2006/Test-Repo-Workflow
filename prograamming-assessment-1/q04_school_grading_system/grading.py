def get_grade(marks):
    if marks < 25:
        return "F"
    if marks < 45:
        return "E"
    if marks < 50:
        return "D"
    if marks < 60:
        return "C"
    if marks <= 80:
        return "B"
    return "A"
