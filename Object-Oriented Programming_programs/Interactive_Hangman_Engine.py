class HangmanEngine:
    def __init__(self, word: str):
        self.word = word.upper()
        self.guessed_letters = set()
        self.chances_left = 6
        self.status = "playing"
    def guess_letter(self, char: str) -> dict:
        letter = char.upper()
        if letter in self.guessed_letters:
            feedback = "Already guessed!"
        else:
            self.guessed_letters.add(letter)
            if letter in self.word:
                feedback = "Correct!"
            else:
                self.chances_left -= 1
                feedback = "Incorrect!"
        clue_letters = []
        for letter_in_word in self.word:
            if letter_in_word in self.guessed_letters:
                clue_letters.append(letter_in_word)
            else:
                clue_letters.append("_")
        clue = " ".join(clue_letters)
        if "_" not in clue_letters:
            self.status = "won"
        elif self.chances_left == 0:
            self.status = "lost"
        return {
            "clue": clue,
            "chances_left": self.chances_left,
            "feedback": feedback,
            "status": self.status,
        }
