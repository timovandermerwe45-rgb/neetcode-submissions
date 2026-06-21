class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for n in nums:
            count_dict[n] = 1 + count_dict.get(n, 0)

        sorted_keys = sorted(count_dict, key=count_dict.get, reverse=True)

        return_l = []
        for i in range(k):
           return_l.append(sorted_keys[i])

        return return_l
        


        