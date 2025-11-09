# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        num_nodes = 0
        while temp:
            num_nodes += 1
            temp = temp.next

        for i in range(num_nodes // 2):
            head = head.next

        return head
