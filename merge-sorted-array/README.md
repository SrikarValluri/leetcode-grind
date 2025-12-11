# merge sorted array

In the original solution, I solved the problem without considering the limited space complexity. I solved this problem similar to the merge sort algorithm, in which we compare and add to a new list until one of the lists is empty, and then dump either of the other lists to the end to complete the merge. However, there's a better solution that doesn't require more than O(1) extra space. Basically, we know that the amount of empty space in nums1 is n, and lets consider the following case:

ex  nums1 = [1,3,4,0,0,0], m = 3, nums2 = [2,5,6], n = 3
if we were to replace greatest values starting from end of nums1, it would work perfectly
[1, 3, 4, 0, 0, 6]
[1, 3, 4, 0, 5, 6]
[1, 3, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]

Worst cases are that a) everything in nums1 less than nums2. In this case, nums will auto-occupy the rightmost part of nums1 or b) left is greater, in which case it'll essentially be shifted to the right, and nums2 will replace left (assuming we keep track of ending index of each)

This is implemented in soln 2.
