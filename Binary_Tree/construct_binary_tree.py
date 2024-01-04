# Given two integer arrays inorder and postorder 
# where inorder is the inorder traversal of a binary tree and 
# postorder is the postorder traversal of the same tree, construct and return the binary tree.

# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# find root in postorder list
# find left and right subtree in Inorder list
# keep slicing off both list to construct subtree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        val = postorder[-1]
        root = TreeNode(val)

        pos = inorder.index(val)
        leftIn = inorder[0:pos]
        rightIn = inorder[pos+1 : len(inorder)]

        leftPost = postorder[0 : len(leftIn)]
        rightPost = postorder[len(leftIn):len(leftIn)+len(rightIn)]

        root.left = self.buildTree(leftIn, leftPost)
        root.right = self.buildTree(rightIn, rightPost)

        return root