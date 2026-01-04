class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        tsum = 0

        for num in nums:
            sum = 0
            count = 0

            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    count += 1
                    sum += i
                    if i * i != num:
                        count += 1
                        sum += num // i
                
                if count > 4: break
            
            if count == 4:
                tsum += sum
            
        return tsum