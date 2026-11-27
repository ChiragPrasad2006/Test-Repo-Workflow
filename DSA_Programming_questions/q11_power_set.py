def power_set(nums: list[int]) -> list[list[int]]:
    result = [[]]
    for number in nums:
        current_length = len(result)
        for index in range(current_length):
            result.append(result[index] + [number])
    return result
