"""
Description
Given a string S, find the length of the longest substring T that contains at most k distinct characters.
"""

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # begin记录起点，cnt记录不同字符数目
        begin = cnt = 0
        # vis记录每个字符的ASCII码对应的出现次数
        vis = [0] * 150 #using ASCII, could also use hashmap, but his would be easier to manage
        ans = 0
        n = len(s)
        for i in range(n):
            if vis[ord(s[i])] == 0:
                cnt += 1
            vis[ord(s[i])] += 1
            while cnt > k:
                # 若不同字符数目超过k，begin后移直到不同字符数目不超过k
                vis[ord(s[begin])] -= 1
                if vis[ord(s[begin])] == 0:
                    cnt -= 1
                begin += 1
            # 更新最大长度
            ans = max(ans, i - begin + 1)
        return ans