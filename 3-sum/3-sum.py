class Solution:
    def twoSum(self, nums, target):
        seen = set()
        res = []
        for x in nums:
            if target - x in seen:
                a, b = target - x, x
                if a <= b:
                    res.append([a, b])
                else:
                    res.append([b, a])
            seen.add(x)
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        banned = set()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break

            two = self.twoSum(nums[i+1:], -nums[i])

            for pair in two:
                trip = [nums[i]] + pair
                trip_tuple = tuple(trip)

                if trip_tuple not in banned:
                    res.append(trip)
                    banned.add(trip_tuple)

        return res
