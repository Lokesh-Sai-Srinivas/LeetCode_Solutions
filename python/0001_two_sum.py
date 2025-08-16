# Problem: 0001 - Two Sum
# Description: Finds indices of two numbers in a list that add up to a target.
# Date: 2025-08-13


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i , num in enumerate(nums):
            c = target - num
            if c in seen:
                return [seen[c] , i]
            seen[num] = i
        
        
