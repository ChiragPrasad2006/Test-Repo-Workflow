class WordReverser:
    def reverse_words(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)
