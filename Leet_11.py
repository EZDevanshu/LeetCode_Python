from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0 , len(height) - 1

        maxHeight = 0

        while l < r :
            num = min(height[r] , height[l])
            currHeight = num * (r - l) 
            maxHeight = max(maxHeight , currHeight)
            if height[l] > height[r] :
                r -= 1
            elif height[l] == height[r] :
                r -= 1
                l += 1
            else :
                l += 1
        return maxHeight

height = [1,8,6,2,5,4,8,3,7] 

obj = Solution()
print(obj.maxArea(height))