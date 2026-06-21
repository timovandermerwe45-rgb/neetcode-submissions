class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexed_nums = []
        for i, num in enumerate(nums):
            indexed_nums.append((i, num))

        sorted_nums = sorted(indexed_nums, key=lambda x: x[1])

        left, right = 0, len(nums)-1

        while left < right:
            if sorted_nums[left][1] + sorted_nums[right][1] == target:
                return sorted([sorted_nums[left][0], sorted_nums[right][0]])
            elif sorted_nums[left][1] + sorted_nums[right][1] < target:
                left += 1
            elif sorted_nums[left][1] + sorted_nums[right][1] > target:
                right -= 1