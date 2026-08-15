class Solution:
    def elevatorRequests(self, n: int , requests: list[int]) -> int:
        sec = 0
        init = 0
        for i in range(len(requests)) :
            sec += abs(requests[i] - init)
            init = requests[i]

        return sec