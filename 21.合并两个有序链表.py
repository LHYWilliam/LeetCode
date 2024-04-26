#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        answer, temp = None, None
        while list1 or list2:
            unable = [one for one in [list1, list2] if one]
            goal = min(unable, key=lambda one: one.val)

            if temp:
                temp.next = ListNode()  # type: ignore
                temp = temp.next
            else:
                temp = ListNode()  # type: ignore
                answer = temp

            temp.val = goal.val

            if goal is list1:
                list1 = list1 if not list1 else list1.next
            else:
                list2 = list2 if not list2 else list2.next

        return answer


# @lc code=end
