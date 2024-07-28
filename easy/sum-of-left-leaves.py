# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def calculate(node: Optional[TreeNode], isLeft: bool) -> None:
            if not node:
                return

            calculate(node.left, True)
            calculate(node.right, False)

            if isLeft and (not node.left and not node.right):
                self.sum += node.val

        calculate(root, False)
        return self.sum
        