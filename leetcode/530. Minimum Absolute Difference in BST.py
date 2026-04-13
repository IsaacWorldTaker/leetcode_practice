from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.last = None
        self.min = inf
        self.recurse(root)
        return self.min

    def recurse(self, root: Optional[TreeNode]):
        if root:
            self.recurse(root.left)
            if self.last is not None:
                self.min = min(abs(root.val-self.last), self.min)

            self.last = root.val

            self.recurse(root.right)


# Example 1
tree_node_1 = TreeNode(1)
tree_node_3 = TreeNode(3)
tree_node_2 = TreeNode(2, tree_node_1, tree_node_3)
tree_node_6 = TreeNode(6)
# tree_node_5 = TreeNode(5)
root_4 = TreeNode(4, tree_node_2, tree_node_6)


# Example 2
tree_node_0 = TreeNode(0)
tree_node_12 = TreeNode(12)
tree_node_49 = TreeNode(49)
tree_node_48 = TreeNode(48, tree_node_12, tree_node_49)
root_1 = TreeNode(1, tree_node_0, tree_node_49)


solution = Solution()
print(solution.getMinimumDifference(root_4))
print(solution.getMinimumDifference(root_1))
