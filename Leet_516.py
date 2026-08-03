class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        row = len(s)
        t = s[::-1]
        col = len(t)

        dp = [[0] * (col + 1) for i in range(row + 1)] 

        for i in range(1 , row + 1) :
            for j in range(1 , col + 1) :
                if s[i - 1] == t[j - 1] :
                    dp[i][j] =1 + dp[i - 1][j - 1]
                else :
                    dp[i][j] = max(dp[i - 1][j] , dp[i][j - 1])
        
        return dp[row][col]