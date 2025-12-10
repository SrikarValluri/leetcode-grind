from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict, s_dict, left, min_str = defaultdict(int), defaultdict(int), 0, None
        for char in t:
            t_dict[char] += 1

        for right, char in enumerate(s):
            if char in t_dict:
                s_dict[char] += 1
            while all(key in s_dict and t_dict[key] <= s_dict[key] for key in t_dict):
                if s[left] in s_dict:
                    s_dict[s[left]] -= 1
                left += 1
                if min_str is None or len(min_str) > (right-left+1):
                    min_str = s[left-1:right+1]

        return min_str if min_str != None else ""
