class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, cur, res = 0, 1, 0
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(prev, cur)
                prev, cur = cur, 1
        
        res += min(prev, cur)
        return res