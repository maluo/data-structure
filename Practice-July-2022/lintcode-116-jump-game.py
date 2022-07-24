# Solution 1 DFS, clean code
class Solution:
    """
    @param a: A list of integers
    @return: A boolean
    """
    def can_jump(self, a):
        # write your code here
        if a == None or len(a) == 0:
            return False
        return self.dfs(a,0)
    
    def dfs (self,a,curIndex):
        if (curIndex == len(a) - 1):
            return True
        count = curIndex + 1
        while count <= curIndex + a[curIndex]:
            if(self.dfs(a,count)):
                return True
            count += 1
        return False
    
# Solution 2 max jump with while -> fast solution, O(N)

class Solution1:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if len(A) == 0:
            return 0
        maxJump, i = A[0], 0
        while i < len(A):
            if maxJump >= len(A) - 1:
                return True
            if maxJump == i : #why?原地踏步情况，无线循环 SINCE LAST i+A[i] = maxJump
                return False
            if i < maxJump:
                maxJump = max(i+A[i], maxJump)
                i += 1
        return False