# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([q])
        q2 = deque([p])

        while q1 and q2:
            nodeQ = q1.popleft()
            nodeP = q2.popleft()

            if nodeQ is None and nodeP is None:
                continue
            if nodeQ is None or nodeP is None or nodeQ.val != nodeP.val:
                return False

            q1.append(nodeQ.left)
            q1.append(nodeQ.right)
            q2.append(nodeP.left)
            q2.append(nodeP.right)
        return True