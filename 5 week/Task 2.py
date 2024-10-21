#37. Sudoku Solver
#https://leetcode.com/problems/sudoku-solver/description/?envType=problem-list-v2&envId=hash-table
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def dfs(position: int):
            if position == len(empty_positions):
                self.is_solved = True
                return

            row_index, col_index = empty_positions[position]

            for value in range(9):
                if (not rows_used[row_index][value] and
                        not cols_used[col_index][value] and
                        not blocks_used[row_index // 3][col_index // 3][value]):
                    rows_used[row_index][value] = cols_used[col_index][value] = \
                    blocks_used[row_index // 3][col_index // 3][value] = True
                    board[row_index][col_index] = str(value + 1)

                    dfs(position + 1)

                    rows_used[row_index][value] = cols_used[col_index][value] = \
                    blocks_used[row_index // 3][col_index // 3][value] = False

                if self.is_solved:
                    return

        rows_used = [[False] * 9 for _ in range(9)]
        cols_used = [[False] * 9 for _ in range(9)]
        blocks_used = [[[False] * 9 for _a in range(3)] for _b in range(3)]

        empty_positions = []
        self.is_solved = False

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    empty_positions.append((row, col))
                else:
                    value = int(board[row][col]) - 1
                    rows_used[row][value] = cols_used[col][value] = blocks_used[row // 3][col // 3][value] = True

        dfs(0)
