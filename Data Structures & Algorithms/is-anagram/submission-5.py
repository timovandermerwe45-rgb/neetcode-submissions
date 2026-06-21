class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for s_i in s:
            s_dict[s_i] = 1 + s_dict.get(s_i, 0)

        for t_i in t:
            t_dict[t_i] = 1 + t_dict.get(t_i, 0)

        for z in s_dict.keys():
            print(z, end='')

        return s_dict == t_dict
        