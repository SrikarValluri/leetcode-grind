class Solution:
    def longestPalindrome(self, s: str) -> int:
        num_chars = defaultdict(int)
        for char in s:
            num_chars[char] += 1

        longest_palindrome = 0
        is_odd = 0
        for char, val in num_chars.items():
            if val % 2 == 0:
                longest_palindrome += val
            else:
                is_odd = 1
                longest_palindrome += val-1

        return longest_palindrome+is_odd
        
