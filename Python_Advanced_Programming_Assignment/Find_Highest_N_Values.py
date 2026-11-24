def highest_n_values(d: dict[str, int], n: int) -> list[tuple[str, int]]:
    pairs = sorted(d.items(), key=lambda item: (-item[1], item[0]))
    return pairs[:n]
