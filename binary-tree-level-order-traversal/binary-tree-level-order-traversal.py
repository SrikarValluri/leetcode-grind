# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        def bfs(start_node):
            visited = set()  # To keep track of visited nodes
            queue = deque([(start_node, 0)])  # Initialize queue with the start node
            visited.add(start_node)
            traversal_order = defaultdict(list)

            while queue:
                current_node, level = queue.popleft()  # Dequeue a node
                traversal_order[level].append(current_node.val)
                left = current_node.left
                right = current_node.right
                if left not in visited and left is not None:
                    visited.add(left)
                    queue.append((left, level+1))  # Enqueue unvisited neighbors

                if right not in visited and right is not None:
                    visited.add(right)
                    queue.append((right, level+1))  # Enqueue unvisited neighbors
            return list(traversal_order.values())

        return bfs(root)
