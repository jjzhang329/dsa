# You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
# Return the root node of the BST after the insertion. 
# It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, 
# as long as the tree remains a BST after insertion. You can return any of them.

# 701. Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

# Approach: always insert the new node as leaf, compare the values to see if left or right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None: 
            node = TreeNode(val)
            return node
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root