class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        streak = 0
        for i in nums:
            if i == 0:
                streak += 1
            else:
                count += streak * (streak + 1)//2
                streak = 0
        count += streak *( streak + 1) // 2
        return count