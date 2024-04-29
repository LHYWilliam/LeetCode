#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:  # type: ignore
        treeA, treeB = [], []

        while headA:
            treeA.append(headA)
            headA = headA.next

        while headB:
            treeB.append(headB)
            headB = headB.next

        position = None
        for node in treeA:
            if node in treeB:
                position = treeB.index(node)

            if position != None:
                position = treeB[position]
                break

        return position


# @lc code=end
