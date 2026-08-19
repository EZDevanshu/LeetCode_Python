class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        li = [] 

        li2 = s.split()

        for i in range(len(li2)) :
            if i >= k :
                break
            li.append(li2[i])
        
        return " ".join(li)