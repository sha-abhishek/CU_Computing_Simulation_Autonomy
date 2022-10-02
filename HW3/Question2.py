class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def solution(root):
    """ Using DFS for node traversal """
    depth = 0
    if root == None:
        return depth

    else:
        depth_left = solution(root.left)
        depth_right = solution(root.right)

        if depth_right > depth_left:
            depth = depth_right + 1
            
        else:
            depth = depth_left + 1
        
    return depth

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
print(solution(a3))