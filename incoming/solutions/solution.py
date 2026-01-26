class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)

        minDif = 1000000
        ans = []

        for idx in range(1, len(arr)):
            diff = arr[idx] - arr[idx - 1]
            if diff < minDif:
                minDif = diff
                ans = [] 

            if minDif == diff:
                ans.append([arr[idx - 1], arr[idx]])

        return ans
