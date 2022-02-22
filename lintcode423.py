class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        stack = []
        for c in s:
            if c == '(' :
                stack.append(')')
            if c == '[' :
                stack.append(']')
            if c == '{' :
                stack.append('}')
            
            if c == ')' or c == ']' or c == '}':
                if not stack or c != stack.pop():
                    return False
        
        return not stack