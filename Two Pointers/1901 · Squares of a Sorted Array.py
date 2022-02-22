"""
Description:
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
"""

"""

"""


class Solution:
    """
    @param A: The array A.
    @return: The array of the squares.
    """

    def SquareArray(self, nums):
        i, j, output = 0, len(nums)-1, [0] * len(nums)

        while i <= j:
            a, b = nums[i]**2, nums[j]**2
            output[j-i] = max(a, b)
            i, j = i + (a > b), j - (not a > b)
        return output
