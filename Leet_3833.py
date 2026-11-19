class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        c = 0
        n = len(nums) - 1
        total = sum(nums) 
        if n < 1 :
            return 0
        for i in range(n) :

            total -= nums[i] 
            avg = total / (n - i)

            if nums[i] > avg :
                c += 1
        
        return c