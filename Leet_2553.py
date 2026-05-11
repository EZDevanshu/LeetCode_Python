class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)) :
            num = str(nums[i])
        
            for i in num :
                digit = int(i)
                res.append(digit)
        
        return res
