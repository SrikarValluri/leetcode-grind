class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, longest = 0, 0
        visited = set()
        for right in range(n):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            longest = max(longest, right-left+1)

        return longest
