class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top , bottom , left , right = 0 , len(matrix) - 1 , 0 , len(matrix[0]) - 1
        li = []
        while top <= bottom and left <= right :
            for i in range(left , right + 1) :
                li.append(matrix[top][i])
            top += 1

            for j in range(top , bottom + 1) :
                li.append(matrix[j][right]) 
            right -= 1

            if top <= bottom :
                for x in range(right , left - 1 , -1) :
                    li.append(matrix[bottom][x])
                bottom -= 1
            if left <= right :
                for k in range(bottom , top - 1 , -1) :
                    li.append(matrix[k][left])
                left += 1
            
        return li