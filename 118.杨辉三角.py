#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:  # type: ignore
        if numRows == 1:
            answer = [[1]]
        if numRows == 2:
            answer = [[1], [1, 1]]
        if numRows >= 3:
            answer = [[1], [1, 1]]

            for i in range(numRows - 2):
                answer.append(
                    [1] + [i + j for i, j in zip(answer[-1][:-1], answer[-1][1:])] + [1]
                )

        return answer


# @lc code=end
