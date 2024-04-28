#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:  # type: ignore
        if rowIndex == 0:
            answer = [1]
        if rowIndex == 1:
            answer = [1, 1]
        if rowIndex >= 2:
            answer = [1, 1]

            for i in range(rowIndex - 2 + 1):
                answer[1:-1] = [i + j for i, j in zip(answer[:-1], answer[1:])]

        return answer


# @lc code=end
