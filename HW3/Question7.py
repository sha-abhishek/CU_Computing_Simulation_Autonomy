# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def nodeval(self):
        return self.val
    
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root==None:
            print(root.nodeval())
        return


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
s.hasPathSum(a3,12)
