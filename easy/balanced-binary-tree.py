# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calculate(root: Optional[TreeNode]) -> tuple[bool, int]:    
            if not root:
                return [True, 0]

            left, right = calculate(root.left), calculate(root.right)
            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return is_balanced, max(left[1], right[1]) + 1

        return calculate(root)[0]
