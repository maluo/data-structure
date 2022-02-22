"""
list(hash.keys()) function -> understnad this function
"""

class Solution:
    """
    @param names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):
        # write your code here
        
        name_set = set()
        j = 0
        for name in names:
            
            if name.lower() not in name_set:
                name_set.add( name.lower() )
                names[j] = name.lower()
                j += 1 
            
        return names[0:j]
    
class Solution1:
    """
    @param names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):
        # write your code here
        hash = {}

        for i in range(len(names)):
            if names[i].lower() in hash:
                continue
            else:
                hash[names[i].lower()] = 1

        return list(hash.keys())    