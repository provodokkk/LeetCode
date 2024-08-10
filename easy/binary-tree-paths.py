# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def dfs(node: Optional[TreeNode], current_path: List[int]):
            if not node:
                return

            current_path.append(node.val)
            
            # if it's a leaf - add the path
            if not node.left and not node.right:
                self.paths.append('->'.join(map(str, current_path)))

            dfs(node.left, current_path)
            dfs(node.right, current_path)

            # when moving backwards - remove the last visited node
            current_path.pop()

        self.paths = []
        dfs(root, [])
        return self.paths
