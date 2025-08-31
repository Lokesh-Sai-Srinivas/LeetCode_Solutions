"""
Problem: 37 - Sudoku Solver  
Description: Write a program to solve a 9×9 Sudoku puzzle by filling the empty cells. Each digit from 1 to 9 must appear exactly once in each row, column, and 3×3 sub-box. The input board may contain empty cells denoted by '.'. The solution must modify the board in-place.  
Date: 2025-08-31
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # bitmask for rows, cols, boxes: 1<<d means digit d+1 is used
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9
        empties = []

        # initialize masks and empty list
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    d = int(board[r][c]) - 1
                    bit = 1 << d
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r//3)*3 + c//3] |= bit

        def dfs(k=0):
            if k == len(empties):
                return True

            # choose empty with fewest candidates
            best = k
            min_opts = 10
            for i in range(k, len(empties)):
                r, c = empties[i]
                used = rows[r] | cols[c] | boxes[(r//3)*3 + c//3]
                opts = 9 - bin(used).count('1')
                if opts < min_opts:
                    min_opts, best = opts, i
                    if opts == 1:
                        break

            # swap best to position k
            empties[k], empties[best] = empties[best], empties[k]
            r, c = empties[k]
            mask_idx = (r//3)*3 + c//3
            used = rows[r] | cols[c] | boxes[mask_idx]

            # try each candidate digit
            for d in range(9):
                bit = 1 << d
                if not (used & bit):
                    board[r][c] = str(d+1)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[mask_idx] |= bit

                    if dfs(k+1):
                        return True

                    # backtrack
                    board[r][c] = '.'
                    rows[r] ^= bit
                    cols[c] ^= bit
                    boxes[mask_idx] ^= bit

            # restore order before returning
            empties[k], empties[best] = empties[best], empties[k]
            return False

        dfs()
