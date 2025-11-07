from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numz = defaultdict(int)
        for num in nums:
            numz[num] += 1

        return max(numz, key=numz.get)
