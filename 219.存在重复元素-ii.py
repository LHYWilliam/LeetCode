#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:  # type: ignore
        answer = {}
        flag = False

        for i in range(len(nums)):
            if nums[i] in answer:
                for j in answer[nums[i]]:
                    if abs(i - j) <= k:
                        flag = True
                        break
                answer[nums[i]].append(i)

            else:
                answer[nums[i]] = [i]

        return flag


# @lc code=end
