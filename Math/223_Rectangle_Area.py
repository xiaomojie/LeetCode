"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
"""
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = (C-A)*(D-B) + (G-E)*(H-F)
        left = max(A,E)
        right = max(min(C,G),left)
        bottom = max(B,F)
        top = max(min(D,H),bottom)
        # print(left,right,top,bottom)
        return area - (right-left)*(top-bottom)

print(Solution().computeArea(-3,0,3,4,0,-1,9,2))
print(Solution().computeArea(-2,-2,2,2,3,3,4,4))