#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sn, tn = 0, 0
        sr, tr = {}, {}
        sa, ta = [], []
        for i, j in zip(s, t):
            if i in sr:
                sa.append(sr[i])
            else:
                sa.append(sn)
                sr[i] = sn
                sn += 1

            if j in tr:
                ta.append(tr[j])
            else:
                ta.append(tn)
                tr[j] = tn
                tn += 1

        return sa == ta


# @lc code=end
