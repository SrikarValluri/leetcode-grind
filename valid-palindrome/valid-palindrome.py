class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = [char.lower() for char in s if char.isalnum()]
        n = len(phrase)
        if n == 0:
            return True
        left, right = 0, n-1
        while (left != right) and (left != len(phrase) // 2 + 1):
            if phrase[left] != phrase[right]:
                return False
            left += 1
            right -= 1
        return True
