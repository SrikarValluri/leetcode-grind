# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1+max(self.height(root.left), self.height(root.right))
        return 0
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left) - self.height(root.right)) <= 1
        return True


              
