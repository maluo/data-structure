"""
Description
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. You need to output the maximum average value.
"""

"""
Notice that array is continous, easily figure out from drawing a graph
range function is open boundary on the right side
"""

class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def findMaxAverage(self, nums, k):
        max_k_sum = running_k_sum = sum(nums[:k])
        
        for i in range(1, len(nums)):
            if i + k <= len(nums):
                running_k_sum += nums[i+k-1] - nums[i-1]
                max_k_sum = max(max_k_sum, running_k_sum)
                
        return max_k_sum / k