"""
递归方法：

例如“ABCDEF”，假设A+B=C，第一次划分，A、B、CDEF，A+B!=CDEF，此时可从CDEF中找出是否有前A、B的和，如果有，
也即C，那么前面就可以是符合条件的串，接下来就看B、C、DEF能不能拆成符合条件的划分，由于少了一个元素，而且
将前2个元素也划分好了，也即我们的问题变成了一个子问题。如此就可以一直递归下去。

"""
class Solution:
    def check(self, s1, s2, s3):
        if (len(s1) > 1 and s1[0]=='0') or (len(s2) > 1 and s2[0]=='0') or (len(s3) > 1 and s3[0]=='0'):
            return False
        sum = str(int(s1) + int(s2))
        if sum == s3:
            return True
        if len(sum) > len(s3) or sum != s3[0:len(sum)]:
            return False
        else:
            return self.check(s2, s3[0:len(sum)], s3[len(sum):])

    def isAdditiveNumber(self, num):
        for i in range(0, len(num)-2):
            for j in range(i+1, len(num)-1):
                if self.check(num[0:i+1], num[i+1:j+1], num[j+1:]):
                    return True
        return False


print(Solution().isAdditive("112358"))
print(Solution().isAdditive("199100199"))

