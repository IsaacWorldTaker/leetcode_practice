from typing import Optional
from collections import deque


def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'Tree: {self.val} | L: {self.left.val}, R: {self.right.val}'


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            temp = root.right
            root.right = root.left
            root.left = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root


example_1 = build_tree([4, 2, 7, 1, 3, 6, 9])
example_2 = build_tree([2, 1, 3])
example_3 = build_tree([])

solution = Solution()

print(solution.invertTree(example_1))
print(solution.invertTree(example_2))
print(solution.invertTree(example_3))
