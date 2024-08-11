# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.result = TreeNode(0)
        def dfs_postorder(node: 'TreeNode') -> bool:
            if not node:
                return False
            
            left = dfs_postorder(node.left)
            right = dfs_postorder(node.right)
            current = (node == p or node == q)

            if (left and right) or (current and right) or (current and left):
                self.result = node
            return left or right or current

        dfs_postorder(root)
        return self.result
    