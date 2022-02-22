"""
merge sort
"""

class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        # write your code here
        tmp = [0] * len(A)
        self.count = 0
        self.mergesort(A, 0, len(A) - 1, tmp)
        return self.count
    
    def mergesort(self, A, start, end, tmp):
        if start >= end:
            return
        
        mid = start + (end - start) // 2
        self.mergesort(A, start, mid, tmp)
        self.mergesort(A, mid + 1, end, tmp)
        self.merge(A, start, end, tmp)
        
    def merge(self, A, start, end, tmp):
        mid = start + (end - start) // 2
        i = start
        j = mid + 1 
        index = start
        while i <= mid and j <= end:
            if A[i] > A[j]:
                tmp[index] = A[j]
                j += 1 
                self.count += mid - i + 1 
            else:
                tmp[index] = A[i]
                i += 1 
                
            index += 1 
        
        while i <= mid:
            tmp[index] = A[i]
            i += 1 
            index += 1 
            
        while j <= end:
            tmp[index] = A[j]
            j += 1 
            index += 1 
        
        for i in range(start, end + 1):
            A[i] = tmp[i]