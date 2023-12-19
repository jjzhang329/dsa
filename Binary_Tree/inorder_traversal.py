# traverse the binary tree in order: left, root, right

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        # left = self.inorderTraversal(root.left)
        # right = self.inorderTraversal(root.right)
        # return left + [root.val] + right

        result = []
        stack = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                result.append(node.val)
                current = node.right
        
        return result