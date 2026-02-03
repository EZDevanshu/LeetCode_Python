from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s :
            return ""

        have = {}
        need = Counter(t)

        required = len(need)
        formed = 0

        l = 0
        min_len = float("inf")
        start = 0
        for r in range(len(s)) :
            ch = s[r]
            have[ch] = have.get(ch , 0) + 1

            if ch in need and have[ch] == need[ch] :
                formed += 1

            while required == formed :
                if r - l + 1 < min_len :
                    min_len = r - l + 1 
                    start = l
                
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]] :
                    formed -= 1

                l  += 1
        return "" if min_len == float("inf") else s[start: start + min_len]
