class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 or len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for s_i in s:
            if s_i not in s_dict:
                s_dict[s_i] = 1
            else:
                s_dict[s_i] = s_dict[s_i] + 1

        for t_i in t:
            if t_i not in t_dict:
                t_dict[t_i] = 1
            else:
                t_dict[t_i] = t_dict[t_i] + 1

        return s_dict == t_dict