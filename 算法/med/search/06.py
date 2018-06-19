class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        ret_int = []
        for i in range(len(intervals)):
            if ret_int[-1].end >= intervals[i].start:
                ret_int[-1].end = max(ret_int[-1].end,intervals[i].end)
            else:
                ret_int.append(intervals[i])

        return ret_int


l1 =  [[1,3],[5,6],[3,10],[15,18]]
l2 = [Interval(1,3),Interval(2,6),Interval(3,10),Interval(15,18)]
l1.sort()
print(l1)
l2.sort(key=lambda x:x.start)
print([[val.start, val.end]for val in l2])
sol = Solution()
print([[val.start, val.end]for val in sol.merge(l2)])
