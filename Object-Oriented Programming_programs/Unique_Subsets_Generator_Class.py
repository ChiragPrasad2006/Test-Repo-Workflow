class SubsetGenerator:
    def get_subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = [[]]
        for number in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [number])
            subsets.extend(new_subsets)
        return subsets
