"""
1.sort by start first, no need to compare start again
2.pops the current i if swap, working on the same interval array
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param: intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        # O(nlogn)时间复杂度, O(1) extra space
        i = 1
        l = len(intervals)
        intervals = sorted(intervals, key = lambda x: x.start)
        while i < l and l > 1:
            # print i, l, intervals
            start, end = intervals[i].start, intervals[i].end
            prevStart, prevEnd = intervals[i-1].start, intervals[i-1].end
            # print start, end, prevStart, prevEnd
            if prevEnd < start:
                i += 1
                continue
            intervals[i-1].end = max(prevEnd, end)
            intervals.pop(i)
            l -= 1
        return intervals