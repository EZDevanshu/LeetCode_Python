class Solution:
    def sumCounts(self, nums: List[int]) -> int: 
        li = []
        for i in range(len(nums)) :
            for j in range(i, len(nums)  + 1) :
               li.append(len(set(nums[i:j]))**2)
        return sum(li)         