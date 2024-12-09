#114. Flatten Binary Tree to Linked List
#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=problem-list-v2&envId=binary-tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = root.right
                root.right = root.left
                root.left = None
            root = root.right