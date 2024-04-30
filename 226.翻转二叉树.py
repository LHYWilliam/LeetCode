#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  # type: ignore
        from queue import Queue

        back = []
        nodes = Queue()
        if root:
            nodes.put(root)
        while not nodes.empty():
            node = nodes.get()
            back.append(node)

            if node.left:
                nodes.put(node.left)
            if node.right:
                nodes.put(node.right)

        for node in back:
            back = node.left
            node.left = node.right
            node.right = back

        return root


# @lc code=end
