class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(row, col):
            if row >= len(grid) or col >= len(grid[0]) or \
                row < 0 or col < 0 or grid[row][col] == 0:
                return 1
            if (row, col) in visit:
                return 0
            visit.add((row, col))
            perim = dfs(row, col + 1)
            perim += dfs(row, col - 1)
            perim += dfs(row + 1, col)
            perim += dfs(row - 1, col)
            return perim
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)