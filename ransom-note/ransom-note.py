from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)
        for letter in magazine:
            mag[letter] += 1

        for letter in ransomNote:
            mag[letter] -= 1

        for val in mag.values():
            if val < 0:
                return False

        return True
