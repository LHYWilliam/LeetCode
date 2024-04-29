#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        rule = {
            num: character
            for num, character in zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        }

        answer = ""
        while (columnNumber - 1) // 26 != 0:
            answer = rule[(columnNumber - 1) % 26] + answer
            columnNumber = (columnNumber - 1) // 26

        answer = rule[(columnNumber - 1) % 26] + answer

        return answer


# @lc code=end
