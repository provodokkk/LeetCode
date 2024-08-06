# Time Complexity: O(m * n)

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.m, self.n = len(grid), len(grid[0])
        result = 0
        self.visited = [[False] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]:
                    result = max(result, self.findLocalMaxGold(i, j, grid))
        
        return result

    def findLocalMaxGold(self, i, j, grid):
        if self.m <= i or i < 0 or \
           self.n <= j or j < 0 or \
           grid[i][j] == 0 or self.visited[i][j]:
            return 0

        self.visited[i][j] = True

        left = self.findLocalMaxGold(i, j - 1, grid)
        right = self.findLocalMaxGold(i, j + 1, grid)
        up = self.findLocalMaxGold(i - 1, j, grid)
        down = self.findLocalMaxGold(i + 1, j, grid)

        self.visited[i][j] = False

        return max(left, right, up, down) + grid[i][j]
