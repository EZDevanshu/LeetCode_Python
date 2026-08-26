class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        di = Counter(nums)
        total = 0
        for i in di :
            if di[i] == 1 :
                total += i
        
        return total
