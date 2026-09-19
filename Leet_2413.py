class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        mini=999
        if(n==1):
            return 2
        if(n%2!=0):
            for i in range(2,n,2):
                if((n*i)<=mini):
                    mini=n*i
            return mini
        else:
            return n