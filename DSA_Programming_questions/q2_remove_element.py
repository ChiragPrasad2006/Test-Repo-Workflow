def remove_element(nums: list[int], val: int) -> int:
    write_index = 0
    for number in nums:
        if number != val:
            nums[write_index] = number
            write_index += 1
    return write_index
