class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return early for differing lengths
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        # iterate through s first
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        # then iterate through t
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        
        # compare s vs t
        for char in s_dict:
            # return if characters don't match
            if char not in t_dict:
                return False
            # return if count of characters doesn't match
            if s_dict[char] != t_dict[char]:
                return False

        return True