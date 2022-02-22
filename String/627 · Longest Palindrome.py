class Solution:
    
    def longestPalindrome(self, s):
        
        table = set()
        for c in s:
            if c in table:
                table.remove(c) 
            else:
                table.add(c)
        even = len(s) - len(table)
        
        return even+1 if len(table) > 0 else even