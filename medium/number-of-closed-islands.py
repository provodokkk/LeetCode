# Time Complexity: O(m * n)

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 

        def dfs(grid: List[List[int]], i: int, j: int) -> bool:
            # if it's a water
            if grid[i][j] == 1:
                return True

            # if the land cell is a border
            if (i == 0 or i == m - 1) or (j == 0 or j == n - 1):
                return False

            # mark the visited cell as water
            grid[i][j] = 1

            up = dfs(grid, i - 1, j)
            down = dfs(grid, i + 1, j)
            left = dfs(grid, i, j - 1)
            right = dfs(grid, i, j + 1)

            return up and down and left and right


        count = 0

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and dfs(grid, i, j):
                    count += 1
                
        return count
