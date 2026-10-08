class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    land[(row, col)] = False
        
        num_islands = 0
        for val in land:
            if land[val]:
                continue
            num_islands += 1
            to_visit = []
            to_visit.append(val)
            while to_visit:
                row, col = to_visit.pop()
                land[(row, col)] = True
                if row > 0 and grid[row - 1][col] == "1" and not land[(row - 1, col)]: # up
                    to_visit.append((row - 1, col))
                if row < len(grid) - 1 and grid[row + 1][col] == "1" and not land[(row + 1, col)]: # down
                    to_visit.append((row + 1, col))
                if col > 0 and grid[row][col - 1] == "1" and not land[(row, col - 1)]: # left
                    to_visit.append((row, col - 1))
                if col < len(grid[0]) - 1 and grid[row][col + 1] == "1" and not land[(row, col + 1)]:
                    to_visit.append((row, col + 1))
        return num_islands
            