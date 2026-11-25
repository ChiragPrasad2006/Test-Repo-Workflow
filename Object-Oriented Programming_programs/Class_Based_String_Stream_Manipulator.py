class IOString:
    def __init__(self):
        self.text = ""
    def get_string(self, s: str) -> None:
        self.text = s
    def print_reversed_string(self) -> str:
        return self.text[::-1]
