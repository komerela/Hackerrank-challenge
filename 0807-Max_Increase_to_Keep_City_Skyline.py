class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        x = range(len(grid)) #Always square "grid.length = grid[0].length"
        gridT = [[grid[j][i] for j in x] for i in x]
        increase = 0
        for i in x:
            for j in x:
                increase += (min([max(grid[i]), max(gridT[j])]) - grid[i][j])
        return increase