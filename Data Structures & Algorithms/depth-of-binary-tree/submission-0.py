# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        y = deque()
        if root:
            y.append(root)

        depth = 0
        while y:
            for i in range(len(y)):
                node = y.popleft()
                if node.left:
                    y.append(node.left)
                if node.right:
                    y.append(node.right)
            depth += 1
        return depth