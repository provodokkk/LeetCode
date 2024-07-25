# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
            if not left_node and not right_node:
                return True
            elif not left_node or not right_node:
                return False

            return (left_node.val == right_node.val) and \
                    dfs(left_node.left, right_node.right) and \
                    dfs(right_node.left, left_node.right)

        return dfs(root.left, root.right)
