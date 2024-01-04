# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# 513. Find Bottom Left Tree Value 
# https://leetcode.com/problems/find-bottom-left-tree-value/description/

# the bottom left value not necessarry the left node
# using bfs to traverse each level and return the first value
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result