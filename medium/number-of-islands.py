# Time Complexity: O(m * n)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        count = 0

        def helper(grid, i, j):
            if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            helper(grid, i - 1, j)
            helper(grid, i + 1, j)
            helper(grid, i, j - 1)
            helper(grid, i, j + 1)


        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    count += 1
                    helper(grid, i, j)

        return count
