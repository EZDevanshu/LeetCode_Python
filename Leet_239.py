from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # store indices
        res = []

        for i in range(len(nums)):

            # 1. remove out-of-window index
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. maintain decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. add current index
            dq.append(i)

            # 4. window complete → take max
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
