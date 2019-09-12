# -*- coding:utf-8 -*-
class Solution:
    def merge(self, left, right):
        i, j = 0, 0
        res = []
        count = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                while j < len(right) and left[i] > 2 * right[j]:
                    count += (len(left) - i)
                    res.append(right[j])
                    j += 1
                else:
                    if j < len(right) and left[i] >= right[j]:
                        k = i + 1
                        while k < len(left) and left[k] <= 2 * right[j]:
                            k += 1
                        count += (len(left) - k)
                        res.append(right[j])
                        j += 1

        res += left[i:] or right[j:]
        return res, count

    def sort(self, data):
        # write code here
        if not data or len(data) <= 1:
            return data, 0

        mid = len(data) // 2
        left, n1 = self.sort(data[:mid])
        right, n2 = self.sort(data[mid:])
        res, n3 = self.merge(left, right)
        return res, n1 + n2 + n3

    def reversePairs(self, nums):
        res, count = self.sort(nums)
        return count

if __name__=='__main__':
    print(Solution().reversePairs([1,3,2,3,1]))
    print(Solution().reversePairs([2,4,3,5,1]))
    print(Solution().reversePairs([5,4,3,2,1]))
    print(Solution().reversePairs([-5, -5]))