def validate_string_strength(s: str, min_length: int) -> bool:
    has_uppercase = lambda text: any(character.isupper() for character in text)
    has_lowercase = lambda text: any(character.islower() for character in text)
    has_number = lambda text: any(character.isdigit() for character in text)
    long_enough = lambda text: len(text) >= min_length
    return has_uppercase(s) and has_lowercase(s) and has_number(s) and long_enough(s)
