class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        m = len(grid)
        n = len(grid[0])
        INF = 2**31 - 1

        queue = deque()
        for row in range(m):
            for col in range(n):
                if not grid[row][col]:
                    queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()
            val = grid[row][col]
            if row > 0 and grid[row-1][col] == INF: #up
                grid[row-1][col] = 1 + val
                queue.append((row-1, col))
            if row < m-1 and grid[row+1][col] == INF: #down
                grid[row+1][col] = 1 + val
                queue.append((row+1, col))
            if col > 0 and grid[row][col-1] == INF: #left
                grid[row][col-1] = 1 + val
                queue.append((row, col-1))
            if col < n-1 and grid[row][col+1] == INF: #right
                grid[row][col+1] = 1 + val
                queue.append((row, col+1))