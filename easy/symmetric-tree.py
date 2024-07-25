# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        return self.traverse(root.left, []) == self.traverse(root.right, [], False)

    def traverse(self, root: Optional[TreeNode], stack: list[int], direction_left: bool = True) -> list[int]:
        if root:
            stack.append(root.val)
            if direction_left:
                self.traverse(root.left, stack)
                self.traverse(root.right, stack)
            else:
                self.traverse(root.right, stack, False)
                self.traverse(root.left, stack, False)
        else:
            stack.append(None)
        return stack
