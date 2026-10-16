class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found


#         class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        seen = {}
#        for i, value in enumerate(nums): #1
#            remaining = target - nums[i] #2
           
#            if remaining in seen: #3
#                return [i, seen[remaining]]  #4
#            else:
#                seen[value] = i