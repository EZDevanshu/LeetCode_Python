class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def backtrack(node) :
            if not node :
                return 0
            
            left = backtrack(node.left)
            right = backtrack(node.right)
            
            self.res = max(self.res , left + right)

            return 1 + max(left , right)

        backtrack(root)
        return self.res
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def backtrack(node) :
            if not node :
                return 0
            
            left = backtrack(node.left)
            right = backtrack(node.right)
            
            self.res = max(self.res , left + right)

            return 1 + max(left , right)

        backtrack(root)
        return self.res
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def backtrack(node) :
            if not node :
                return 0
            
            left = backtrack(node.left)
            right = backtrack(node.right)
            
            self.res = max(self.res , left + right)

            return 1 + max(left , right)

        backtrack(root)
        return self.res
