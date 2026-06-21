class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_dict = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in s_dict:
                s_dict[sorted_s] = [s]
            else:
                #temp = s_dict[sorted_s]
                #temp.append(s)
                #s_dict[sorted_s] = temp
                s_dict[sorted_s].append(s)

            

        return list(s_dict.values())
        