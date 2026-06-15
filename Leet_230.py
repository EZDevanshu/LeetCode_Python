# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.visit = 0
        self.ans = None
    
        def inOrder(node) :
            if node is None:
                return
            inOrder(node.left)
            self.visit+= 1
            if self.visit == k :
                self.ans = node.val
                return 
            inOrder(node.right)
        inOrder(root)
        return self.ans
            
