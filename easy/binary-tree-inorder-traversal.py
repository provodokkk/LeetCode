# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []

        def add_to_stack(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return
            stack.append(root.val)
            add_to_stack(root.left)

            res.append(stack.pop())
            add_to_stack(root.right)

        add_to_stack(root)
        return res
        