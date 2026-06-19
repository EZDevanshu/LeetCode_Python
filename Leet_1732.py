class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0 
        current = 0

        for i in gain :
            current += i 
            maxi = max(maxi , current)
        return maxi