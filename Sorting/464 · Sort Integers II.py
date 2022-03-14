"""
Description
Given an integer array, sort it in ascending order in place. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

Wechat reply the 【464】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

Example
Example1:

Input: [3, 2, 1, 4, 5], 
Output: [1, 2, 3, 4, 5].
Example2:

Input: [2, 3, 1], 
Output: [1, 2, 3].
"""
class heapSort(object):
    def __init__(self,nums):
        self.A = nums
        self.size = len(nums)
        self.buildHeap()
        for i in range(self.size-1,-1,-1):
            self.A[0],self.A[i] = self.A[i],self.A[0]
            self.size -= 1
            self.heapify(0)
        
    def parent(self,i):
        return (i-1)/2
        
    def left(self,i):
        return i*2 + 1
        
    def right(self,i):
        return i*2 + 2
        
    def heapify(self,i):
        l,r = self.left(i),self.right(i)
        largest = i
        if l < self.size and self.A[l] > self.A[largest]:
            largest = l
        if r < self.size and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            self.A[largest],self.A[i] = self.A[i],self.A[largest]
            self.heapify(largest)
    def buildHeap(self):
        for i in range(self.size-1,-1,-1):
            self.heapify(i)


"""
Two pointer with recursion, quick sort
标准双指针算法

"""            
class quickSort(object):
    def __init__(self,nums):
        self.A = nums
        self.sort(0,len(self.A)-1)
        
    def sort(self,start,end):
        if start >= end:
            return 
        l,r = start,end
        pivot = self.A[ l + (r-l)/2 ]
        while l <= r:
            while l<=r and self.A[l] < pivot:
                l += 1
            while l<=r and self.A[r] > pivot:
                r -= 1
            if l <= r:
                self.A[l],self.A[r] = self.A[r],self.A[l]
                l += 1
                r -= 1
        self.sort(start,r)
        self.sort(l,end)


"""
参考ipad 九章算法笔记
"""    
class mergeSort(object):
    def __init__(self,nums):
        self.A = nums
        size = len(self.A)
        self.temp = [0 for _ in range(size)]
        self.sort(0,size-1)

        
    def sort(self,start,end):
        if start >= end:
            return 
        mid = start + (end-start)/2
        self.sort(start,mid)
        self.sort(mid+1,end)
        self.merge(start,end)
        
    def merge(self,start,end):
        mid = start + (end-start)/2
        l,r = start,mid+1
        index = start
        while l<=mid and r<=end:
            if self.A[l] < self.A[r]:
                self.temp[index] = self.A[l]
                index += 1
                l += 1
            else:
                self.temp[index] = self.A[r]
                index += 1
                r += 1
        while l<=mid:
            self.temp[index] = self.A[l]
            index += 1
            l += 1
        while r<=end:
            self.temp[index] = self.A[r]
            index += 1
            r += 1
        for i in range(start,end+1):
            self.A[i] = self.temp[i]

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        #heapSort(A)
        #quickSort(A)
        mergeSort(A)