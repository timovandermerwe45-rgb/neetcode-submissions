class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for n in nums:
            count_dict[n] = count_dict.get(n, 0) + 1

        sorted_keys = sorted(count_dict, key=count_dict.get, reverse=True)

        print(count_dict)
        print(sorted_keys)

        return sorted_keys[:k]
        