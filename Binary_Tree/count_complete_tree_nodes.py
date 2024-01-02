# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        # check if a full tree
        left = root.left
        right = root.right
        leftDepth = 0
        rightDepth = 0
        while left:
            left = left.left
            leftDepth += 1
        while right:
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth:
            return (2 << leftDepth) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)