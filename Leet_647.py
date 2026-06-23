class Solution:
    def countSubstrings(self, s: str) -> int:
        li = []

        for i in range(len(s)) :
            res = ""
            for j in range(i , len(s)) :
                res += s[j]
                li.append(res)

        count = 0
        for x in li :
            if x[::-1] == x :
                count += 1    

        return count  