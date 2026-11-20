def check_eligibility(classes_held, classes_attended):
    percentage = round(classes_attended / classes_held * 100, 1)
    return percentage, percentage >= 75
