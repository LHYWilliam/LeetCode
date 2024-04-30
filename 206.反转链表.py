#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        answer = ListNode()  # type: ignore
        temp = answer
        for node in reversed(nodes):
            temp.next = node
            temp = temp.next
        temp.next = None

        return answer.next


# @lc code=end
