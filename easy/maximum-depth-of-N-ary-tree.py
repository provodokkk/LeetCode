# Time Complexity: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node: 'Node') -> int:
            if not node:
                return 0

            max_child_depth = 0
            for c in node.children:
                max_child_depth = max(max_child_depth, dfs(c))
            
            return max_child_depth + 1
        
        return dfs(root)
