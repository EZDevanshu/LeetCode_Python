class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        return min(360 - abs((hour * 30) + minutes * 0.5  - minutes * 6) , abs(hour * 30 + minutes * 0.5 - minutes * 6 ))