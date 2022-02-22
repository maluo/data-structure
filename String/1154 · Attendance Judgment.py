class Solution:
    """
    @param record: Attendance record.
    @return: If the student should be punished return true, else return false. 
    """
    def judge(self, record: str) -> bool:
        # Write your code here.
        cntD, cntL = 0, 0
        for s in record:
            if s == 'D':
                cntD += 1
            if s == 'L':
                cntL += 1
            if s != 'L':
                cntL = 0
            if cntD >= 2 or cntL == 3:
                return True
        return False
