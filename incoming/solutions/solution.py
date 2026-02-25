class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i] += 10001*arr[i].bit_count()
        arr.sort()
        for i in range(len(arr)):
            arr[i] %= 10001
        return arr
