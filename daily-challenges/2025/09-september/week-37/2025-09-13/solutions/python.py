class Solution:
    def maxFreqSum(self, s: str) -> int:
        arr = [0] * 26  

        for ch in s:
            arr[ord(ch) - ord('a')] += 1

        freq1 = 0  
        freq2 = 0  

        for i in range(26):
            if i in [ord('a') - ord('a'), ord('e') - ord('a'), ord('i') - ord('a'), ord('o') - ord('a'), ord('u') - ord('a')]:
                freq1 = max(freq1, arr[i])
            else:
                freq2 = max(freq2, arr[i])

        return freq1 + freq2