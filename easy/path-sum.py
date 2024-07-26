# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root: Optional[TreeNode], currentSum: int) -> bool:
            if not root:
                return False

            currentSum += root.val
            if not root.left and not root.right:
                return targetSum == currentSum

            if (helper(root.left, currentSum) or helper(root.right, currentSum)):
                return True

        return helper(root, 0)
            