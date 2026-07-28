class Solution:
    def smallestPalindrome(self, s: str) -> str:
        alfa = [0] * 26

        for ch in s:
            alfa[ord(ch) - ord('a')] += 1

        first = []
        middle = ""

        for i in range(26):
            first.extend(chr(i + ord('a')) * (alfa[i] // 2))
            if alfa[i] % 2 == 1:
                middle = chr(i + ord('a'))

        second = first[::-1]

        return "".join(first) + middle + "".join(second)