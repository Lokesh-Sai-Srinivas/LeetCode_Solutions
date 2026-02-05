class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        result = [0] * n 
        for i in range(n):
            idx = ((i + nums[i]) % n + n) % n 
            result[i] = nums[idx] 
        return result