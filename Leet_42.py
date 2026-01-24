from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        l , r = 0 , len(height) - 1
        maxLeft = height[0]
        maxRight = height[len(height) - 1]
        tap = 0
        while l < r :
            if maxLeft < maxRight :
                l += 1
                maxLeft = max(maxLeft , height[l])
                tap += maxLeft - height[l]
            else :
                r -= 1
                maxRight = max(maxRight , height[r])
                tap += maxRight - height[r]
        return tap
height = [0,1,0,2,1,0,1,3,2,1,2,1]
obj = Solution()
print(obj.trap(height))