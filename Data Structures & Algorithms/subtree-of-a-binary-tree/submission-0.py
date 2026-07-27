# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False  # ran out of tree without finding a match

        if self.isSameTree(root, subRoot):
            return True

        # not a match here — check if subRoot exists deeper in either subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, a, b):
        if not a and not b:
            return True  # both empty — identical (trivially)
        if not a or not b:
            return False  # one is empty, the other isn't — can't match
        if a.val != b.val:
            return False  # values differ — can't match

        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)