class Solution:
    def romanToInt(self, s: str) -> int:
        RTI = { "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
        }
        SC = {
            "I": {"V", "X"},
            "X": {"L", "C"},
            "C": {"D", "M"}
        }
        total = 0
        prev = "M"
        for char in s:
            for let in SC:
                if prev == let and char in SC[let]:
                    total -= 2*RTI[prev]
                    break

            total += RTI[char]
            prev = char

        return total
