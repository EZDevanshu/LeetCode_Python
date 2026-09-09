class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n)) < 4 :
            return 0

        comma = 0
        i = 1000
        while i <= n :
            comma += n - i + 1
            i *= 1000
        return comma