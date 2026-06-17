class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n , m = len(p) , len(s)

        if n > m :
            return res

        p_freq = [0] * 26
        for i in p :
            p_freq[ord(i) - ord('a')] += 1

        s_freq = [0] * 26
        for i in s[:n] :
            s_freq[ord(i) - ord('a')] += 1

        if p_freq == s_freq :
            res.append(0)

        for i in range(n,m) :
            s_freq[ord(s[i]) - ord('a')] += 1
            s_freq[ord(s[i - n]) - ord('a')] -= 1 

            if s_freq == p_freq :
                res.append(i - n + 1)
        return res

