"""
Description
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.
"""

"""
经典sliding window,先扩大有边界，再逐步缩小左边界
"""

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        left = 0

        curr_sum = 0

        res = float('inf')

        for right in range(len(nums)):

            # 滑窗右边界扩张

            curr_sum += nums[right]

            # 满足条件

            while curr_sum >= s:

                # 更新res

                res = min(res, right - left + 1)

                # 滑窗左边界收缩

                curr_sum -= nums[left]

                left += 1

        return -1 if res == float('inf') else res