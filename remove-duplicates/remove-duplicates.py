class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        prev = None
        while i < len(nums):
            if nums[i] == prev:
                nums.pop(i)
                continue
            prev = nums[i]
            i += 1
