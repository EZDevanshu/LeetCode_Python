class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for i in s :
            if i == "*" :
                if result :
                    result.pop()
            elif i == "#" :
                result += result.copy()
            elif i == "%" :
                result = result[::-1]
            else :
                result.append(i)
        return "".join(result)