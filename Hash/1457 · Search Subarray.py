"""
Description
Given an array arr and a nonnegative integer k, you need to find a continuous array from this array so that the sum of this array is k. Output the length of this array. If there are multiple such substrings, return the one with the minimum ending position; if there are multiple answers, return the one with the minimum starting position. If no such subarray is found, -1 is returned.

Input：arr=[1,2,3,4,5] ，k=5
Output：2
Explanation:
In this array, the earliest contiguous substring is [2,3] since 2+3 = 5.

最早前缀和
"""

class Solution:
    """
    @param arr: The array 
    @param k: the sum 
    @return: The length of the array
    """

    def lent(self, arr):
        return len(arr)

    def searchSubarray(self, arr, k):
        # Write your code here
        n = self.lent(arr)
        sum = 0
        maps = {}
        maps[sum] = 0;
        st = n + 5;
        len = 0;
        for i in range(0, n):
            sum += arr[i]
            if sum - k in maps:
                if (st > maps[sum - k]):
                    st = maps[sum - k]
                    len = i + 1 - maps[sum - k]
            if sum not in maps:
                maps[sum] = i + 1;

        if (st == n + 5):
            return -1;
        else:
            return len;