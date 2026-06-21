class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()  # Use a set to automatically handle duplicate triplets
        nums.sort()

        for i, num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = num + nums[left] + nums[right]

                if current_sum == 0:
                    # Convert to a tuple so it can be added to the set
                    res.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

        # Convert the set of tuples back into a list of lists
        return [list(triplet) for triplet in res]
        