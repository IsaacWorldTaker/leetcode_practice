from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        parents = set()
        nodes = {}
        for group in descriptions:
            child = nodes.get(group[1]) or TreeNode(group[1])
            node = nodes.get(group[0]) or TreeNode(group[0])
            if group[2] == 1:  # is left
                node.left = child
            else:
                node.right = child
            nodes[node.val] = node
            nodes[child.val] = child
            if node not in children:
                parents.add(node)
            children.add(child)
            if child in parents:
                parents.remove(child)

        return parents.pop()


solution = Solution()
print(solution.createBinaryTree(
    [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]))
print(solution.createBinaryTree(
    [[1, 2, 1], [2, 3, 0], [3, 4, 1]]))
