"""
求给定的num是否是一个数的平方。
牛顿迭代法求平方根：
设r是函数y=f(x)的根，使用牛顿迭代法，给定一个初始值x0，过x0做切线，y = f(x0) + f'(x0)(x-x0)，求
该切线与x轴的交点x1 = x0 - f(x0)/f'(x0),称x1为r的一次近似值，再过(x1,f(x1))做切线。以此循环下去
所以迭代公式为：xn+1 = xn - f(xn)/f'(xn)
对于求平方根，x^2 - n = 0， 可看做函数 f(x) = y = x^2 - n，f'(x) = 2x， 则迭代公式为：
xn+1 = xn - (xn^2 - n)/(2*xn) = xn - xn/2 + n/(2xn) = 1/2(xn + n/xn)
"""

class Solution(object):
    def isPerfectSquare1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r * r > num:
            r = (r + num//r)//2
        return r * r == num

    # 法二：A square number is 1+3+5+7+...
    def isPerfectSquare(self, num):
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

