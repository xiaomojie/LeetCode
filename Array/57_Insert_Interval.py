"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            i += 1

        if i == len(intervals) or intervals[i].start > newInterval.end:
            intervals.insert(i, newInterval)
            return intervals
        else:
            intervals[i].start = min(intervals[i].start, newInterval.start)
            intervals[i].end = max(intervals[i].end, newInterval.end)

        while i + 1 < len(intervals) and intervals[i].end >= intervals[i + 1].start:
            intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
            intervals.remove(intervals[i + 1])

        return intervals


intervals = [Interval(1,3),Interval(6,9)]
results = Solution().insert(intervals, Interval(2,5))
print(results[0].start, results[0].end)



# intervals = [Interval(1,3),Interval(2,6), Interval(8,10), Interval(15,18)]



