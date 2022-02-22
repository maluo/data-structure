class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hash = {}
        for ind, num in enumerate(numbers):
            if target - num in hash:
                return [hash[target - num], ind]
            hash[num] = ind
        return [-1, -1] 


"""
标准双指针模板，一般先排序，然后选择一个判定左位移还是右位移的条件
"""
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if not numbers:
            return -1
        nums = sorted(numbers)
        #print(nums)
        left, right = 0, len(numbers) - 1 
        curSum = 0 # hold nums[l] + nums[r]
        while left < right:
            #print('left, right', left, right)
            curSum = nums[left] + nums[right]
            if curSum == target:
                return [left,right]
                """
                #array.index(x)   Return the smallest i such that i is the index of the first occurrence of x in the array.
                i = numbers.index(nums[left])
                j = numbers.index(nums[right])
                if i == j:  ##两个重复的数字时候，index只能返回最小的指针 ?
                    k = numbers[i+1:].index(nums[right]) + i + 1
                    return [i, k]
                elif i < j:
                    return [i, j] 
                else:
                    return [j, i]
                #return [numbers.index(nums[left]), numbers.index(nums[right])]
                """
            if curSum < target:
                left += 1 
            if curSum > target:
                right -= 1 
        return -1
                
"""
A way to test out the solution
"""
numbers = [0,4,3,0]
target = 0
obj = Solution()
result = obj.twoSum(numbers, 0)
print(result)        