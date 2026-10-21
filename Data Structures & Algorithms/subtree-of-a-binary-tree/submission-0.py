# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False
            
        if self.isSameTree(root, subRoot):
            return True
        else:
            return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not q and not p:
                return True
            
            if p and q and p.val == q.val:
                return (self.isSameTree(p.right, q.right) and self.isSameTree(p.left,q.left))
            else:
                return False
