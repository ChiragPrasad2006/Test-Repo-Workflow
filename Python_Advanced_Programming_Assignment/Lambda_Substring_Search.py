def filter_by_substring(words: list[str], target: str) -> list[str]:
    return list(filter(lambda word: target in word, words))
