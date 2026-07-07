class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def knapsack(arr, i , curSum) :
            if  i == len(nums) :
                return 1 if target == curSum else 0
            
            return knapsack(arr , i + 1 , curSum - arr[i]) + knapsack(arr , i + 1 , curSum + arr[i]) 
        return knapsack(arr , 0 , 0)   