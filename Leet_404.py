class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        t = 0

        if root.left :
            if root.left.left is None and root.left.right is None :
                t += root.left.val
        return t + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

