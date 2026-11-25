class CowsAndBullsGame:
    def __init__(self, secret: str):
        self.secret = secret
        self.guesses = 0
    def guess(self, attempt: str) -> dict:
        self.guesses += 1
        cows = 0
        bulls = 0
        for index in range(len(self.secret)):
            if attempt[index] == self.secret[index]:
                cows += 1
            elif attempt[index] in self.secret:
                bulls += 1
        return {
            "cows": cows,
            "bulls": bulls,
            "guesses": self.guesses,
            "game_over": cows == len(self.secret),
        }
