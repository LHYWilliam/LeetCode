#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = True
        if len(s) == len(t) and set(s) == set(t):
            stimes, ttimes = {}, {}
            for one in set(s):
                stimes.update({one: s.count(one)})
            for one in set(t):
                ttimes.update({one: t.count(one)})

            for one in set(s):
                flag = stimes[one] == ttimes[one]

        else:
            flag = False

        return flag


# @lc code=end
