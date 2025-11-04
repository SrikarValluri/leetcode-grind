class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        counterparts = set(pairs.values())
        for char in s:
            if char in counterparts:
                stack.append(char)
            else: 
                if stack == [] or stack.pop() != pairs[char]:
                    return False

        return True if stack == [] else False
