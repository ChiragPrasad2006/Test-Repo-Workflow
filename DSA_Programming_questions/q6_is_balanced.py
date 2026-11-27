def is_balanced(s: str) -> bool:
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}
    for character in s:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack.pop() != matching[character]:
                return False
    return len(stack) == 0
