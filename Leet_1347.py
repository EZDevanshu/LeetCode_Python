class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqS = [0] * 26
        freqT = [0] * 26

        for i in range(len(s)) :
            freqS[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)) :
            freqT[ord(t[i]) - ord('a')] += 1

        ans = 0
        for i in range(len(freqT)) :
            ans += abs(freqS[i] - freqT[i])

        return ans // 2
        