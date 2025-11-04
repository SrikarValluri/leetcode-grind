class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two = {}
        for i in range(len(nums)):
            if target-nums[i] in two:
                return [two[target-nums[i]], i]
            else:
                two[nums[i]] = i
