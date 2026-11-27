def get_score(secret: str, guess: str) -> tuple[int, int]:
    cows = 0
    for index in range(4):
        if secret[index] == guess[index]:
            cows += 1
    bulls = len(set(secret) & set(guess)) - cows
    return cows, bulls
