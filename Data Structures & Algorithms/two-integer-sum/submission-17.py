class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j, n in enumerate(nums):
                if nums[i] + nums[j] == target and i != j:
                    return[i, j]
        