#98. Validate Binary Search Tree
#https://leetcode.com/problems/validate-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def in_order_traversal(node):
            nonlocal last_value_visited
            if node is None:
                return True

            if not in_order_traversal(node.left):
                return False

            if last_value_visited >= node.val:
                return False

            last_value_visited = node.val

            if not in_order_traversal(node.right):
                return False

            return True

        last_value_visited = float('-inf')

        return in_order_traversal(root)