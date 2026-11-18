class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        m = 1
        inc = 1 
        for i in range(1, len(nums)) :
            if nums[i] > nums[i - 1] :
                inc += 1
            else :
                m = max(inc , m)
                inc = 1

        # m = max(inc , m)

        dec = 1 
        for i in range(1, len(nums)) :
            if nums[i] < nums[i - 1] :
                dec += 1
            else :
                m = max(m , dec)
                dec = 1

        return max(dec , inc , m)
        
