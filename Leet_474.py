class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for i in range(m + 1)] 

        for i in strs :
            zCnt = i.count("0")
            oCnt = i.count("1")
        
            for i in range(m, zCnt - 1 , -1) :
                for j in range(n, oCnt - 1, -1) :
                    dp[i][j] = max(dp[i][j] , 1 + dp[i - zCnt][j - oCnt])
            
        return dp[m][n]