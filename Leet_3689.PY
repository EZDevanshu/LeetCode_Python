class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ans = max(nums) - min(nums)

        return ans * k