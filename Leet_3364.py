class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini = float('inf')
        for i in range(len(nums)) :
            ans = 0
            for j in range(i , len(nums)) :
                ans += nums[j]

                if j - i + 1 >= l and j - i + 1 <= r and ans > 0 :
                    mini = min(mini , ans)
        return -1 if mini == float('inf') else mini