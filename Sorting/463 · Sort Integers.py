"""
Bubble sort: move small ones to left one by one
把最小的值不断往左边移动
"""

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        n = len(A)
        
        for i in range(n-1):
            for j in range(0,n-i-1): # pops up small ones to left one by one
                if A[j] > A[j+1]:
                    A[j],A[j+1] = A[j+1],A[j]
        
        return A