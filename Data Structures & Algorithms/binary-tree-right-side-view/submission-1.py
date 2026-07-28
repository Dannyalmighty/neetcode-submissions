# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # q = collections.deque([root])

        # while q:
        #     rightSide = None
        #     qLen = len(q)

        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node:
        #             rightSide = node
        #             q.append(node.left)
        #             q.append(node.right)
        #     if rightSide:
        #         res.append(rightSide.val)
        # return res

        result = []

        def dfs(node, depth):
            if not node:
                return

            # first time reaching this depth means it's the rightmost node seen so far
            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)  # visit right FIRST
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result