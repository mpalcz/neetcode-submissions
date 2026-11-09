class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if sr >= len(image) or sr < 0 or sc >= len(image[sr]) or sc < 0 or image[sr][sc] == color:
            return image
        adjacent = deque()
        start_color = image[sr][sc]
        adjacent.append((sr, sc))
        while adjacent:
            (row, col) = adjacent.popleft()
            if image[row][col] != start_color:
                continue
            image[row][col] = color
            if row > 0 and image[row - 1][col] == start_color:
                adjacent.append((row - 1, col))
            if row < len(image) - 1 and image[row + 1][col] == start_color:
                adjacent.append((row + 1, col))
            if col > 0 and image[row][col - 1] == start_color:
                adjacent.append((row, col - 1))
            if col < len(image[row]) - 1 and image[row][col + 1] == start_color:
                adjacent.append((row, col + 1)) 
        return image
            
