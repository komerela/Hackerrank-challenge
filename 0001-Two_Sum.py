def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [d[target - n], i]
        else:
            d[n] = i

    """
    Brute Force
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    """   