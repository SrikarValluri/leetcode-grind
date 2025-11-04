from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st_dict = defaultdict(int)

        for char in s:
            st_dict[char] += 1
        for char in t:
            st_dict[char] -= 1

        # make sure now that both dicts have the same numbers
        for k, v in st_dict.items():
            if v != 0:
                return False
        return True
