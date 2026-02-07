class Solution:
    def minimumDeletions(self, s: str) -> int:
        op,bc = 0,0

        for ch in s:
            if ch == 'b': bc += 1
            elif bc > 0 : 
                bc -= 1
                op += 1
        
        return op