def reverse_words(s: str) -> str:
    characters = list(s)
    characters.reverse()
    read_index = 0
    write_index = 0
    while read_index < len(characters):
        if characters[read_index] == " ":
            read_index += 1
        else:
            if write_index > 0:
                characters[write_index] = " "
                write_index += 1
            end_index = read_index
            while end_index < len(characters) and characters[end_index] != " ":
                end_index += 1
            left = read_index
            right = end_index - 1
            while left < right:
                characters[left], characters[right] = characters[right], characters[left]
                left += 1
                right -= 1
            while read_index < end_index:
                characters[write_index] = characters[read_index]
                write_index += 1
                read_index += 1
    return "".join(characters[:write_index])
