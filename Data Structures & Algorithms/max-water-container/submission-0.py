class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = 0

        while left < right:
            #height * width
            area = min(heights[left], heights[right]) * (right-left)
            print(str(min(heights[left], heights[right])) + ',' + str(right-left))
            res = max(res, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return res