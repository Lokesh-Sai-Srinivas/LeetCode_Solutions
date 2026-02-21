class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        mask = 665772 
        count = 0 
        for x in range(left, right + 1): 
            count += (mask >> bin(x).count("1")) & 1 
        return count
