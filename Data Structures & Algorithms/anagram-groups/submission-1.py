class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_maps =[]
        for str in strs:
            temp_map = {}
            for s in str:
                temp_map[s] = 1 + temp_map.get(s, 0)
            strs_maps.append(temp_map)

        group_map = {}
        for i, value in enumerate(strs_maps):
            group_map[i] = []
            for j, strs_map in enumerate(strs_maps):
                if self.isAnagram(value, strs_map):
                    temp = group_map.get(i)
                    temp.append(j)
                    group_map[i] = temp

        group_set = set()
        for g in group_map:
            temp_tuple = tuple(group_map[g])
            if temp_tuple not in group_set:
                group_set.add(temp_tuple)

        return_arr = []
        for g in group_set:
            temp_arr = []
            for t in g:
                temp_arr.append(strs[t])
            return_arr.append(temp_arr)

        return return_arr

        
    def isAnagram(self, str_map1, str_map2):
        if len(str_map1) != len(str_map2):
            return False

        for c in str_map1:
            if str_map1[c] != str_map2.get(c, 0):
                return False

        return True