class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxLength = 0

        for r in range(len(nums)):
            if nums[r] == 0 :
                k -= 1
            if k < 0:
                if nums[l] == 0 :
                    k += 1
                l += 1
            r += 1
            maxLength = max(maxLength , r - l)
        return maxLength