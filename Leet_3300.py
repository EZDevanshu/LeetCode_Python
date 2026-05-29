class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val = float('inf')

        for num in nums :
            t_sum = 0
            while num > 0 :
                t_sum += num % 10 
                num = num // 10
            min_val = min(min_val,t_sum)    
        return min_val