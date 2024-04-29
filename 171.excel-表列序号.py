#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#


# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        rule = {
            character: num
            for character, num in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26))
        }

        answer = 0
        for i in range(len(columnTitle)):
            answer += (rule[columnTitle[i]] + 1) * pow(26, len(columnTitle) - i - 1)

        return answer


# @lc code=end
