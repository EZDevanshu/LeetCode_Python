class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k :  
            li = []

            for i in range(0 , len(s) , k) :
                grp = s[i : i + k]

                grpsum = sum(int(x) for x in grp)

                li.append(str(grpsum))

            s = "".join(li)

        return s

