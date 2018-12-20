class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = sum(nums[0:k])
        res = sums
        for i in range(k, len(nums)):
            # 超时
            # max_sum = max(max_sum, sum(nums[i-k+1:i+1]))
            sums = sums - nums[i-k] + nums[i]
            res = max(sums, res)
        return res/k

print(Solution().findMaxAverage([0,4,0,3,2], 1))
print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
print(Solution().findMaxAverage([5], 1))