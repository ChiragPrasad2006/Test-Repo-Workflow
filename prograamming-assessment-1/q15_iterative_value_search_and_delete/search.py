def search_and_destroy(nums, target):
    for value in nums[:]:
        if value == target:
            nums.remove(value)
    return nums
