import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        new_grid = []
        row = len(grid)
        col = len(grid[0])

        for i in grid :
                new_grid.extend(i)

        k = k % len(new_grid)
        new_grid = new_grid[-k:] + new_grid[:-k]

        matrix = []
        ind = 0 
        for i in range(row) :
            matrix.append(new_grid[ind : ind + col])
            ind += col

        return matrix