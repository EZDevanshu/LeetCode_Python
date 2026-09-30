class Solution:
    def maxDepth(self, s: str) -> int:
        high = 0
        count = 0
        for i in s :
            if i == '(' :
                count += 1
            high = max(count , high)
            if i == ')' :
                count -= 1
                 
        return high