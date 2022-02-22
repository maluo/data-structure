class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        # Write your code here
        # run throught the string, keep appending with a flag
        # meet ' ', set the flag to true
        n = 1
        t = ""
        for i in s:
            if i == " ":
                t = t + i
                n = 1
            elif i != " " and n == 1:
                t = t + i.upper()
                n = 0
            elif i != " " and n == 0:
                t = t + i
        return t

    
class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        
        # Write your code here
        
        def convertCharToStr(arr):
            i, str = 0, ""
            length = len(arr)-1
            
            while(i <= length):
                str += arr[i]
                i+=1

            return str
        
        length,i,flag = len(s)-1, 0, False
        arr = list(s)
        lastChar = ''
        
        while(i <= length):

            if(arr[i] == ' '):
                lastChar = arr[i]
                i += 1
                continue # skip the rest part of the code
            
            # last char ' ', this char not ' ', then uppercase
            if(lastChar == ' ' or i ==0 and arr[i] != ' '):
                arr[i] = arr[i].upper()
                lastChar = arr[i]
            
            i+=1
        
        return convertCharToStr(arr)
    
    

