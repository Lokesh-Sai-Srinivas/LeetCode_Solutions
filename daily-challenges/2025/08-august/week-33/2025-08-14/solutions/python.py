class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9,-1, -1):
            pat = str(i) * 3
            if(num.find(pat) != -1) :
                return pat
        
        return ""