class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1] * (m + 1) for i in range(n + 1)]
        # def lcs(text1 , text2 , n , m , dp) :
        #         return 0
        #     if dp[n][m] != -1 :
        #         return dp[n][m]
            
        #     if text1[n - 1] == text2[m - 1] :
        #         dp[n][m] = 1 + lcs(text1 , text2 , n - 1 , m - 1 ,dp)
        #         return dp[n][m]
        #     else :
        #         dp[n][m] = max(lcs(text1 , text2 , n - 1 , m , dp) , lcs(text1 , text2 , n, m - 1 , dp))
        #         return dp[n][m]
            
        # lcs(text1 , text2 , n , m, dp)
        # return dp[n][m]
        
        for i in range(m + 1) :
            for j in range(n + 1) :
                if i == 0 or j == 0 :
                    dp[i][j] = 0
        for i in range(1, m + 1) :
            for j in range(1 ,n + 1) :        
                if text2[i - 1] == text1[j - 1] :
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else :
                    dp[i][j] = max(dp[i][j - 1] , dp[i - 1][j])

        return dp[m][n]