class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)) :
            temp = sum([int(x) for x in str(nums[i])])
            if temp == i :
                return i
        
        return -1