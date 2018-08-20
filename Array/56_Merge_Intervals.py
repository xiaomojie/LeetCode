"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# Sorting takes O(n log(n)) and merging the intervals takes O(n). So, the resulting algorithm takes O(n log(n)).
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals

        intervals.sort(key=lambda x:x.start)
        results = [intervals[0]]
        i = 1
        j = 0
        while i < len(intervals):
            if results[j].end >= intervals[i].start:
                results[j].end = max(results[j].end, intervals[i].end)
            else:
                results.append(intervals[i])
                j += 1
            i += 1

        return results

# intervals = [Interval(1,3),Interval(2,6), Interval(8,10), Interval(15,18)]
intervals = [Interval(2,3),Interval(2,2), Interval(3, 3), Interval(1,3),Interval(5,7),Interval(2,2),Interval(4,6)]
results = Solution().merge(intervals)
print(results[0].start, results[0].end)
# print(Solution().merge([[1,4],[4,5]]))



