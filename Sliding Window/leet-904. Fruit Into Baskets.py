"""
Work out this one.
"""
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        begin = 0
        cntType = 0 # count type of fruits
        result = 0 # count number of fruits in output
        max_len = 0
        picked = [0] * 10
        for end in range(len(fruits)):
            # can not take,move out the first type and try
            if picked[fruits[end]] == 0 and cntType == 2:
                while picked[begin] != 0:
                    picked[begin] -= 1
                    begin += 1
                cntType -= 1
            # new type
            if picked[fruits[end]] == 0 and cntType < 2:
                cntType += 1
            # intake
            picked[fruits[end]] += 1
            # refresh max_len
            max_len = max(max_len,end - begin + 1)
        return max_len
            
                
    class Solution(object):
        def totalFruit(self, fruits):
            begin = 0
            cntType = 0 # count type of fruits
            max_len = 0
            picked = [0] * 100000
            for end in range(len(fruits)):
                if picked[fruits[end]] == 0:
                    cntType += 1
                picked[fruits[end]] += 1
                while cntType > 2:
                    picked[fruits[begin]] -= 1
                    if picked[fruits[begin]] == 0:
                        cntType -= 1
                    begin += 1
                max_len = max(max_len, end - begin + 1)
            return max_len
            
                
            
            
                
            
    