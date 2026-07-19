class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        n = len(coins)
        dp = [[0] * (amt + 1) for i in range(n + 1)]

        for j in range(amt + 1) :
            dp[0][j] = float("inf")
        
        for i in range(1, n + 1):
            dp[i][0] = 0

        for j in range(1, amt + 1) :
            if j % coins[0] == 0 :
                dp[1][j] = j // coins[0]
            else :
                dp[1][j] = float("inf")

        for i in range(2, n + 1) :
            for j in range(1 ,amt + 1) :
                if coins[i - 1] <= j:
                    dp[i][j] = min(dp[i - 1][j] , 1 + dp[i][j - coins[i - 1]])
                else :
                    dp[i][j] = dp[i - 1][j]
        
        return -1 if dp[n][amt] == float("inf") else dp[n][amt]
