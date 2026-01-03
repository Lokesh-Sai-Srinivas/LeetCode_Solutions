class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        nums = []
        i = 1
        while(True):
            if(self.contains0(n - i) and self.contains0(i)):
                nums.append(i)
                nums.append(n - i)
                break
            else:
                i += 2
        return nums
    
    def contains0(self, n: int) -> bool:
        while(n > 0):
            if n % 10 == 0: 
                return False
            n = n // 10
        return True