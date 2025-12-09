class Solution:
    def myAtoi(self, s: str) -> int:
        s, n, new, i, neg = list(s), len(s), [], 0, False
        while  i < n and s[i] == " ":
            i += 1
        if  i < n and s[i] in {"+", "-"}:
            if s[i] == "-": neg = True
            i += 1
        while i < n and s[i] == 0:
            i += 1
        while i < n and s[i].isnumeric():
            new.append(s[i])
            i += 1

        if new == []:
            return 0

        res = -int("".join(new)) if neg else int("".join(new))

        if res > (2**31 - 1):
            return 2**31 - 1
        elif res < (-2**31):
            return -2**31
        else:
            return res
