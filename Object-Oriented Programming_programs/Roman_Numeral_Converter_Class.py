class RomanConverter:
    def to_roman(self, num: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        result = ""
        for value, numeral in values:
            while num >= value:
                result += numeral
                num -= value
        return result
    def from_roman(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        for index, character in enumerate(s):
            if index + 1 < len(s) and values[character] < values[s[index + 1]]:
                total -= values[character]
            else:
                total += values[character]
        return total
