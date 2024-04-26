#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        rule = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        answer = 0
        visited = [False for _ in range(len(s))]
        for i in range(len(s)):
            if not visited[i]:
                if i == len(s) - 1:
                    answer += rule[s[i]]
                    visited[i] = True
                elif rule[s[i]] >= rule[s[i + 1]]:
                    answer += rule[s[i]]
                    visited[i] = True
                else:
                    answer += rule[s[i + 1]] - rule[s[i]]
                    visited[i + 1] = visited[i] = True

        return answer


# @lc code=end
