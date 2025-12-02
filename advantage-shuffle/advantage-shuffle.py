from collections import deque
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        queue = deque(sorted(nums1))

        for b, i in sorted([[b, i] for i, b in enumerate(nums2)], reverse=True):
            if b < queue[-1]:
                nums2[i] = queue.pop()
            else:
                nums2[i] = queue.popleft()

        return nums2
