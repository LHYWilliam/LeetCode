#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:  # type: ignore
        from queue import Queue

        nodes = Queue()
        nodes.put({"node": root, "sum": root.val})

        flag = False
        while not nodes.empty():
            now = nodes.get()
            node, sum = now["node"], now["sum"]

            if node and not node.left and not node.right and sum == targetSum:
                flag = True
                break

            if node and node.left:
                nodes.put({"node": node.left, "sum": sum + root.left.val})
            if node and node.right:
                nodes.put({"node": node.right, "sum": sum + root.right.val})

        return flag


# @lc code=end
