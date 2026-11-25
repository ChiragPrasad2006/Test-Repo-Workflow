class ThreeSumZero:
    def find_triplets(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                total = nums[index] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return triplets
