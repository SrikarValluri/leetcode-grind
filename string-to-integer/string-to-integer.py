class Solution:
    def myAtoi(self, s: str) -> int:
        while s != "" and s[0] in {" "}:
            s = s[1:]

        if s == "":
            return 0

        neg = False
        if s[0] in {"+", "-"}:
            if s[0] == "-":
                neg = True
            s = s[1:]

        while s != "" and s[0] == "0":
            s = s[1:]

        if s == "":
            return 0

        atoi = ""
        for i in range(len(s)):
            if s[i].isnumeric():
                atoi += s[i]
            else:
                break

        if atoi == "":
            return 0

        atoi = -int(atoi) if neg else int(atoi)

        if atoi > 2**31 - 1:
            return 2**31 - 1
        if atoi < -2**31:
            return -2**31

        return atoi
