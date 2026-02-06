class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort() 
        n = len(nums) 
        ans = 0 
        j = 0 
        for i in range(n):
            while nums[i] > nums[j] * k:
                j += 1 
            ans = max(ans, i - j + 1) 
            
        return n - ans