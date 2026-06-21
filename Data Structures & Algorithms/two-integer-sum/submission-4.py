class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            check = target - n
            if check in map:
                return [map[check], i]
            else:
                map[n] = i