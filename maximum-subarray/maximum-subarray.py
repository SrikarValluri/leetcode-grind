class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]

            if total < 0:
                total = 0

            res = max(total, res)

        if res == 0:
            return max(nums)

        return res
