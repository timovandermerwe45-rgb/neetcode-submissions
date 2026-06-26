class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_a = {}

        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in grouped_a:
                grouped_a[s_sorted].append(s)
            else:
                grouped_a[s_sorted] = [s]
            
        return list(grouped_a.values())
        