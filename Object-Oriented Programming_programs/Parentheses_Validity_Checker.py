class ParenthesesValidator:
    def is_valid(self, s: str) -> bool:
        stack = []
        matching = {")": "(", "}": "{", "]": "["}
        for character in s:
            if character in "({[":
                stack.append(character)
            else:
                if not stack or stack[-1] != matching[character]:
                    return False
                stack.pop()
        return len(stack) == 0
