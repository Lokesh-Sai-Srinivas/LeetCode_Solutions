class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        l = len(nums) - 1
        maxi = 0

        while(s < l) :
            maxi = max((nums[s] + nums[l]), maxi)
            s += 1
            l -= 1
        return maxi