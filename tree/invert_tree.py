# https://leetcode.com/problems/invert-binary-tree/description/

import collections

# Given
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root):

    # Approach 1 DFS
    def dfs(root):
        if not root:
            return

        left = root.left
        right = root.right

        root.left = right
        root.right = left

        dfs(left)
        dfs(right)

    # dfs(root)
    # return root


    # Approach 2 BFS
    queue = collections.deque()

    def bfs(root):

        if not root:
            return 

        queue.append(root)

        while queue:

            node = queue.popleft()
            if node:
                left = node.left
                right = node.right
                queue.append(left)
                queue.append(right)
                node.left = right
                node.right = left

    bfs(root)
    return root
