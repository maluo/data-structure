class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """
    def longestSemiAlternatingSubstring(self, s):
        n = len(s)
        if n < 3:
            return n
        res, cnt = 0, 1
        left = 0
        for right in range(n):
            if right > 0 and s[right] == s[right - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                left = right - 1
                cnt = 2
            res = max(res, right - left + 1)

        return res 

# 同向双指针案例
# 注意求最优解，用最少的便利和对比次数。J无需再往前从头开始推
# 
class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """
    def longestSemiAlternatingSubstring(self, s):
        # write your code here
        if not s :
            return 0
        
        n, j = len(s), 0
        longest = 0
        
        for i in range(n):
        
            while j < n and not self.is_included(s[i:j]):
                j += 1
        
            if j > n :
                break
        
            if self.is_included(s[i:j]): # caused by the last incremental only
                j -= 1
        
            longest = max(longest,j - i)
        
        return longest

    def is_included(self,str):
        return "aaa" in str or "bbb" in str