"""
Problem: 36 - Valid Sudoku  
Description: Given a 9×9 board, determine if it is a valid Sudoku. Only filled cells (‘1’–‘9’) need to be checked: each row, each column, and each of the nine 3×3 sub-boxes must contain no duplicate digits. Empty cells are denoted by '.'.  
Date: 2025-08-30
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue
                d = int(ch) - 1
                b = 3 * (r//3) + (c // 3)
                if (d in row[r] or d in col[c] or d in box[b]):
                    return False
                row[r].add(d)
                col[c].add(d)
                box[b].add(d)
        
        return True
