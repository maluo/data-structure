"""
Description
Given a array A consisting of N integers and an integer K,
return the largest contiguous subarray from all the contiguous subarrays of length K.
We defined that subarray A is greater than subarray B if the first non-matching element in both arrays has a greater value in A than in B.
For example,A=[1,2,4,3],B=[1,2,3,5].
A is greater than B because A[2]>B[2].
"""
"""
A[a:b] -> b is open boundary again, need to put b+1
"""


class Solution:
    """
    @param A: the array
    @param K: the length 
    @return: the largest subarray
    """
    def largestSubarray(self, A, K):
        max_index = 0, K - 1
        for start in range(len(A) - K + 1):
            end = start + K - 1
            if self.is_a_less_than_b(A, (start, end), max_index):
                continue
            max_index = start, end
        return A[max_index[0] : max_index[1] + 1]

    def is_a_less_than_b(self, A, index_a, index_b):
        for i in range(index_a[1] - index_a[0] + 1):
            if A[index_a[0] + i] == A[index_b[0] + i]:
                continue
            return A[index_a[0] + i] < A[index_b[0] + i]
        return False
