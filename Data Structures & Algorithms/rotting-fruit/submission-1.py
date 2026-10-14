class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        minute = 0
        queue = deque()
        not_rotten = set()
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col]:
                    not_rotten.add((row, col))

        if not not_rotten:
            return minute
        if not queue:
            return -1
        
        sub_queue = deque()
        while queue or sub_queue:
            if not queue:
                minute += 1
                while sub_queue:
                    queue.append(sub_queue.popleft())
            (row, col) = queue.popleft()
            if row > 0 and (row-1, col) in not_rotten:
                not_rotten.discard((row-1, col))
                sub_queue.append((row-1, col))
            if row < m-1 and (row+1, col) in not_rotten:
                not_rotten.discard((row+1, col))
                sub_queue.append((row+1, col))
            if col > 0 and (row, col-1) in not_rotten:
                not_rotten.discard((row, col-1))
                sub_queue.append((row, col-1))
            if col < n-1 and (row, col+1) in not_rotten:
                not_rotten.discard((row, col+1))
                sub_queue.append((row, col+1))
        if not_rotten:
            return -1
        return minute
        
