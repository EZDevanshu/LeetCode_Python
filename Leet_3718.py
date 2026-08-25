class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        m = 1
        while True :
            if k * m not in nums :
                return k * m
            m += 1