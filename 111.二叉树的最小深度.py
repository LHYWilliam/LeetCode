#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:  # type: ignore
        from queue import Queue

        answers = []
        nodes = Queue()
        nodes.put({"node": root, "depth": 1})

        while not nodes.empty():
            now = nodes.get()
            node, depth = now["node"], now["depth"]

            if node and not node.left and not node.right:
                answers.append(depth)

            if node and node.left:
                nodes.put({"node": node.left, "depth": depth + 1})
            if node and node.right:
                nodes.put({"node": node.right, "depth": depth + 1})

        return min(answers) if answers else 0


# @lc code=end
