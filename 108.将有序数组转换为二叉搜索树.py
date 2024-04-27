#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root: Optional[TreeNode], num: int) -> None:  # type: ignore
        if root.val > num:
            if not root.left:
                root.left = TreeNode(num)  # type: ignore
            else:
                self.find(root.left, num)

        if root.val < num:
            if not root.right:
                root.right = TreeNode(num)  # type: ignore
            else:
                self.find(root.right, num)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:  # type: ignore
        root = TreeNode(nums[len(nums) // 2])  # type: ignore

        orders = [0, len(nums) // 2, len(nums)]
        for left, right in zip(orders[:-1], orders[1:]):
            self.find(root, nums[(left + right) // 2])
            orders.insert(orders.index(left), (left + right) // 2)

        self.find(root, nums[0])
        self.find(root, nums[-1])

        return root


# @lc code=end
