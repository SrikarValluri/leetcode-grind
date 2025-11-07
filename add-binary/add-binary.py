class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = len(a)-1, len(b)-1
        added = ""
        carry = 0
        while x != -1 or y != -1:
            x_val = 0 if x < 0 else a[x]
            y_val = 0 if y < 0 else b[y]
            digit = int(x_val) + int(y_val) + carry
            added += str(digit % 2)
            carry = digit // 2
            x = max(-1, x-1)
            y = max(-1, y-1)
        if carry:
            added += "1"
        return added[::-1]
