class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        targetFreq = len(nums) // 2 

        di = Counter(nums)

        for i in di:
            if di[i] == targetFreq :
                return i
                