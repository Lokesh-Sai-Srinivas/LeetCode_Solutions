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