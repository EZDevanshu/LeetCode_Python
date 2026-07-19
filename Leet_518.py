class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amt + 1) for i in range(n + 1)]

        for i in range(n + 1) :
            for j in range(amt + 1) :
                if i == 0 and j == 0 :
                    dp[i][j] = 1
                    continue 
                if j == 0 :
                    dp[i][j] = 1
                    continue 
                if i == 0 :
                    dp[i][j] = 0 
                    continue 
                
                if coins[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else :
                    dp[i][j] = dp[i - 1][j]
        
        return dp[i][j]
