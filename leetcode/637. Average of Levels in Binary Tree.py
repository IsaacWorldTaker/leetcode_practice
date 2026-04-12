# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # find nodes in each level
        nodes = deque([root])
        result = []
        sum = 0
        while nodes:
            size = len(nodes)
            for _ in range(size):
                node = nodes.popleft()
                sum += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if size:
                result.append(sum/size)
            sum = 0
        return result


# Example 1
tree_node_7 = TreeNode(7)
tree_node_15 = TreeNode(15)
tree_node_20 = TreeNode(20, tree_node_15, tree_node_7)
tree_node_3 = TreeNode(3)
tree_node_5 = TreeNode(5)
tree_node_13 = TreeNode(17, tree_node_5)
tree_node_9 = TreeNode(9)

root_1 = TreeNode(3, tree_node_9, tree_node_20)

solution = Solution()

print(solution.averageOfLevels(root_1))
