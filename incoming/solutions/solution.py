class Solution:
    def numSteps(self, s: str) -> int:
        ans, car = 0, 0
        for i in range(len(s) - 1, 0, -1) :
            if int( s[i] ) + car == 1:
                car = 1
                ans += 2
            else :
                ans += 1

        return ans + car
