class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        li = [0] * (2 * n) 
        for i in range(n) :
            li[i * 2] = nums[i]
            li[i * 2 + 1] = nums[i + n]
                        
        return li
