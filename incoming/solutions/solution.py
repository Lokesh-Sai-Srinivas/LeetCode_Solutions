class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        a = 1000
        b = 1000

        for i in range(1, len(nums)):
            if nums[i] < a :
                b = a
                a = nums[i]
            elif nums[i] < b :
                b = nums[i]

        return first + a + b
