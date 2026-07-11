class Solution:
    def lastStoneWeightII(self, arr: List[int]) -> int:
        n = len(arr)
        total = sum(arr)
        dp = {}
        def backtrack(i , sum1) :
            if i == n :
                return abs(total - 2 * sum1)

            if (i, sum1) in dp:
                return dp[(i, sum1)]

            take = backtrack(i + 1 , sum1 + arr[i])
            nonTake = backtrack(i + 1 ,sum1)

            dp[(i , sum1)] =  min(take , nonTake)

            return dp[(i , sum1)]
        return backtrack(0,0)   
    


    class Solution:
	def minDifference(self, arr):
		# code here
		n = len(arr)
		total = sum(arr)
		
		def backtrack(i , sum1) :
		    if i == n :
		        return abs(total) - 2 * sum1 
		       
		    take = backtrack(i + 1 ,sum1 + arr[i])
		    non_take = backtrack(i + 1 , sum1)
		    
		    return min(take , non_take)
		
		 return backtrack(0 ,0)   
		 