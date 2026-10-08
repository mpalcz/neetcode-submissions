class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    count = 0
                    landNear = set()
                    landNear.add((row, col))
                    while landNear:
                        isl_row, isl_col = landNear.pop()
                        count += 1
                        grid[isl_row][isl_col] = 0
                        if isl_row > 0 and grid[isl_row - 1][isl_col] and (isl_row - 1, isl_col) not in landNear: #up
                            landNear.add((isl_row - 1, isl_col))
                        if isl_row < len(grid) - 1 and grid[isl_row + 1][isl_col] and (isl_row + 1, isl_col) not in landNear: #down
                            landNear.add((isl_row + 1, isl_col))
                        if isl_col > 0 and grid[isl_row][isl_col - 1] and (isl_row, isl_col - 1) not in landNear: #left
                            landNear.add((isl_row, isl_col - 1))
                        if isl_col < len(grid[0]) - 1 and grid[isl_row][isl_col + 1] and (isl_row, isl_col + 1) not in landNear: #right
                            landNear.add((isl_row, isl_col + 1))
                    maxArea = max(maxArea, count)
        return maxArea




        