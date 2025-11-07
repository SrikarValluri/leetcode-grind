class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1 # there's 1 way to get to the 0th stair, one way to get to the first stair
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2] # you get to the current stair by either the i-1 or i-2th step

        return dp[n]
