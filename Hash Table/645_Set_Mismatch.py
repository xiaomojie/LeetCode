from collections import Counter


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        count = Counter(nums)
        ans.append(count.most_common(1)[0][0])
        # print(ans)
        # print(set(range(1, len(nums)+1)))
        # print(set(nums))
        ans.append((set(range(1, len(nums)+1)) - set(nums)).pop())

        return ans

print(Solution().findErrorNums([1,1]))
print(Solution().findErrorNums([1,2,2,4]))

