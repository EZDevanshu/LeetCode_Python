class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set()
        for ch in sentence:
            alphabet.add(ch)

        return len(alphabet) == 26