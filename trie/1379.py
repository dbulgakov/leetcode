from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([cloned])

        while q:
            node = q.popleft()

            if node.val == target.val:
                return node

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return None
