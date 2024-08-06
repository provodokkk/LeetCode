# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, nums = [root], []

        while stack:
            node = stack.pop()

            if not node:
                continue

            nums.append(node.val)
            stack.append(node.left)
            stack.append(node.right)            

        return nums[::-1]
