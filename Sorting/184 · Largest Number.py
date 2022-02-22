"""
Description
Given a list of non negative integers, arrange them such that they form the largest number.

Wechat reply the 【184】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

The result may be very large, so you need to return a string instead of an integer.

Example
Example 1:

Input:[1, 20, 23, 4, 8]
Output:"8423201"
Example 2:

Input:[4, 6, 65]
Output:"6654"
Challenge
Do it in O(nlogn) time complexity.
"""

class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        # write your code here
        self.mergeSort(0,len(nums)-1,nums)
        res=''.join([str(x) for x in nums])

        return "0" if set(res)=={'0'} else res
    
    def mergeSort(self,start,end,A):
        if start>=end:
            return

        mid=start+(end-start)//2
        self.mergeSort(start,mid,A)
        self.mergeSort(mid+1,end,A)

        l=start
        r=mid+1
        temp=[]

        while l<=mid and r<=end:
            if str(A[l])+str(A[r])>str(A[r])+str(A[l]):
                temp.append(A[l])
                l+=1
                continue
            else:
                temp.append(A[r])
                r+=1
                continue
        
        while l<=mid:
             temp.append(A[l])
             l+=1

        while r<=end:
             temp.append(A[r])
             r+=1

        for i in range(start,end+1):
            A[i]=temp[i-start]