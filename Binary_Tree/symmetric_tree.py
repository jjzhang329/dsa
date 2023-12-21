# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if left == None and right != None: return False
        if left != None and right == None: return False
        if left == None and right == None: return True
        if left.val != right.val: return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)

        return outside and inside