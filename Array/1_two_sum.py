#121
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
# Time:  O(n)
# Space: O(n)
#lalala

def twoSum_1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = dict(zip(nums, list(range(0, len(nums)))))
    for i in range(len(nums)):
        if d.__contains__(target - nums[i]):
            index = d.get(target - nums[i])
            if index != i:
                return sorted([i, index])
    return None


def twoSum_2(nums, target):
    d = {}
    for i in range(len(nums)):
        if d.__contains__(target - nums[i]):
            return [d.get(target - nums[i]), i]
        d[nums[i]] = i
    return None


def twoSum_3(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target-num], i]
        lookup[num] = i


def twoSum_4(nums, target):
    l = list(zip(nums, list(range(0, len(nums)))))
    temp = sorted(l, key=lambda x: x[0])
    i = 0
    j = len(nums)-1
    while i < j:
        if temp[i][0] + temp[j][0] == target:
            return [temp[i][1], temp[j][1]]
        elif temp[i][0] + temp[j][0] > target:
            j -= 1
        else:
            i += 1



print(twoSum_1([1, 2, 3], 4))
print(twoSum_2([1, 2, 3], 4))
print(twoSum_3([1, 2, 3], 4))
print(twoSum_4([1, 2, 3], 4))
