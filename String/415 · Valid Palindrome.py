class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
            # write your code here
            str_s=""
            for i in s.lower():
                if i.isalpha() or i.isdigit():
                    str_s+=i
                    
            reverse_s = str_s[::-1] #reverse the entire string
            if reverse_s == str_s:
                return True
            else:
                return False
            
# Try with two pointer method later            