# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        output = []

        while q:
            qLen = len(q)
            tmp = []
            for i in range (qLen):
                x = q.popleft()
                if x:
                    tmp.append(x.val)
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
            
            if x:
                output.append(tmp)
        
        return output
        