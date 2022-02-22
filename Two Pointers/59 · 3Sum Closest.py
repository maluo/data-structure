"""
配合排序加双指针
"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        res = float('inf')
        numbers.sort()

        for i in range(len(numbers)-2):
            l = i+1 
            r = len(numbers)-1

            while l < r:
                cur  = numbers[i] + numbers[l] + numbers[r]
                if abs(cur-target) < abs(res - target):
                    res = cur
                elif cur < target:
                    l+=1
                else:
                    r-=1
        return res
