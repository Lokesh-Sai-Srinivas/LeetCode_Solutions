class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even_in_n = n // 2
        odd_in_n = n - even_in_n
        even_in_m = m //2
        odd_in_m = m - even_in_m

        return even_in_n * odd_in_m + odd_in_n * even_in_m