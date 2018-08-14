# coding = utf-8
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

# 其实就是求min{ height[i], height[j]} * (j-i)的最大值
# 从两端开始，算面积，然后挑短的移动
# Time:  O(n)
# Space: O(1)


def most_water_1(height):
    i = 0
    j = len(height)-1
    maxarea = 0
    while j > i:
        maxarea = max(maxarea, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maxarea

