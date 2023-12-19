# traverse a binary tree in post order: left, right, root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        # dfs
        # left = self.postorderTraversal(root.left)
        # right = self.postorderTraversal(root.right)

        # return left + right + [root.val]

        # interative, using stack
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            result.append(node.val)
        
        return result[::-1]