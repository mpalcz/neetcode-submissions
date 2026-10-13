class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            seen_row, seen_col, seen_grid = [0]*9, [0]*9, [0]*9
            for j in range(9):
                if (board[i][j] != "." and seen_row[int(board[i][j])-1]) or (board[j][i] != "." and seen_col[int(board[j][i])-1]):
                    return False
                
                if (board[i][j] != "."):
                    seen_row[int(board[i][j])-1] = 1
                if (board[j][i] != "."):
                    seen_col[int(board[j][i])-1] = 1

                # check grid
                row_ind = (j//3) + 3*(i//3)
                col_ind = (j%3) + 3*(i%3)
                if board[row_ind][col_ind] != "." and seen_grid[int(board[row_ind][col_ind])-1]:
                    return False
                if board[row_ind][col_ind] != ".":
                    seen_grid[int(board[row_ind][col_ind])-1] = 1
        return True
                    