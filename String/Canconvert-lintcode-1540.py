class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        # Write your code here
        if(s == None or t == None):
            return False;

        if(len(s) < len(t)):
            return False;

        left, right = len(s)-1, len(t)-1
        i, j = 0, 0
        while (j <= right and i <= left):
            if(s[i] == t[j]):
                i+=1
                j+=1
            else:
                i+=1
        
        return  j == len(t) 
