# diameter of a binary tree

At each and every node, there is the possibility of the maximum diameter to occur between the length left subtree and the length of the right subtree.

I didn't realize this, so my original solution was

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if root:
                left_depth = depth(root.left)
                right_depth = depth(root.right)
                return 1 + max(left_depth, right_depth)
            return 0
        return depth(root.left) + depth(root.right)

But the issue was I was only considering that the maximum diameter would occur at the root node. I wasn't considering it could happen at every possible node. Calculating the depth of a particular subtree is pretty straightforward at this point, so it was just keeping track of every diameter for each node.
