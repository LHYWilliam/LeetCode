#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:  # type: ignore
        answer = ""

        for i in range(min([len(one) for one in strs])):
            flag = True
            temp = strs[0][i]

            for one in strs:
                flag = one[i] == temp
                if not flag:
                    break

            if flag:
                answer += temp
            else:
                break

        return answer


# @lc code=end
