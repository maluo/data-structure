class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        s = set()
        for c in str:
            if c in s:
                return False
            s.add(c)
        return True
            
