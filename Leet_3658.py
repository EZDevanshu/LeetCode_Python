class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        i = 1
        countOdd = 0
        countEven =0
        while countOdd != n and countEven != n :
            if i & 1 == 1 and countOdd != n:
                sumOdd += i
                countOdd +=1 
            elif countEven != n:
                sumEven += i
                countEven += 1
            i+= 1
        mini = min(sumOdd , sumEven)

        def gcd(sumOdd , sumEven , mini) :
            gcd = 1
            for i in range(1, mini + 1) :
                if sumOdd % i == 0 and sumEven % i == 0 :
                    gcd = i
            
            return gcd
        
        return gcd(sumOdd , sumEven , mini)