class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):

        arr = s.split()
        arr.reverse()
        arr_reverse = " ".join(arr) #importnat
        return arr_reverse
    
class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):

        arr = s.split()
        arr.reverse()
        arr_reverse = ""
        for s in arr:
            arr_reverse += s + " "
        arr_reverse = arr_reverse [0:len(arr_reverse)-1] 
        return arr_reverse