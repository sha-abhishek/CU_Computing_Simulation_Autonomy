# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        valid_sum = False
        if root.val == sum and root.left == None and root.right == None:
            return True

        if not root.left == None:
            valid_sum = valid_sum  or Solution().hasPathSum(root.left, sum - root.val)

        if not root.right == None:
            valid_sum  = valid_sum or Solution().hasPathSum(root.right, sum - root.val)

        return valid_sum 


a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a5=TreeNode(5)
a15.left=a5
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20

s = Solution()
print(s.hasPathSum(a3,30))


