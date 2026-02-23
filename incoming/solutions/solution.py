class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        
        for i in range(len(s) - k + 1) :
            st.add(s[i: i + k])
        
        return len(st) == (1 << k)
