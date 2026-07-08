# recursive function


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
#         def knapsack(arr, i , curSum) :
#             if  i == len(nums) :
#                 return 1 if target == curSum else 0
            
#             return knapsack(arr , i + 1 , curSum - arr[i]) + knapsack(arr , i + 1 , curSum + arr[i]) 
#         return knapsack(arr , 0 , 0)   


#  recursive -> memoization (table)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def knapsack(i , curSum) :
            if (i , curSum) in dp :
                return dp[(i,curSum)]

            if  i == len(nums) :
                return 1 if target == curSum else 0
            
            dp[(i , curSum)] = knapsack(i + 1 , curSum - nums[i]) + knapsack(nums , i + 1 , curSum + nums[i]) 
            return dp[(i,curSum)]
        return knapsack(0 , 0)