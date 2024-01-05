# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q 
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Approach: using postorder traversal, pass value back to root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None: return root
        if root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: 
            return root
        elif left == None and right is not None: 
            return right
        elif left is not None and right == None: 
            return left
        else:
            return None