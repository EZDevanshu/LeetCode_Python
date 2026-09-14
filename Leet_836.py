class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1 = rec1[0]
        y1 = rec1[1]
        x2 = rec1[2]
        y2 = rec1[3]
        X1 = rec2[0]
        Y1 = rec2[1]
        X2 = rec2[2]
        Y2 = rec2[3]

        return X1 < x2 and X2 > x1 and Y1 < y2 and Y2 > y1