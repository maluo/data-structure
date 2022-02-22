"""
Description
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.
"""

"""
采用递归可解任意 sum，不论是 3 sum 还是 4 sum 还是 5 sum。
只不过缺点是对于大量数据来说会造成 TLE。原因是 Stack Overflow。我认为可以用记忆化搜索来优化。
"""

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        temp = []
        result = []
        numbers.sort()
        
        self.four_sum(numbers, 0, temp, result, target)
        
        return result
    
    def four_sum(self, nums, start, temp, result, target):
        if len(temp) == 4 and target == 0:
            result.append(temp.copy())  
        end = start
        while end < len(nums):
            if target < nums[end]:
                break
            if end != start and nums[end] == nums[end - 1]:
                end += 1
                continue
            temp.append(nums[end])
            self.four_sum(nums, end + 1, temp, result, target - nums[end])
            temp.pop()
            end += 1
            
"""

"""