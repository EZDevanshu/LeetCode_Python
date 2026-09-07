class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        di = Counter(arr)

        li = []

        for i in di :
            li.append(di[i]) 
        
        for i in range(len(li)) :
            for j in range(i + 1 , len(li)) :
                if li[i] == li[j]:
                    return False 
        
        return True