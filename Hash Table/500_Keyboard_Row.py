class Solution:
    def findWords1(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = ['Q','q','W','w','E','e','R','r','T','t','Y','y','U','u','I','i','O','o','P','p']
        line2 = ['A','a','S','s','D','d','F','f','G','g','H','h','J','j','K','k','L','l']
        line3 = ['Z','z','X','x','C','c','V','v','B','b','N','n','M','m']
        if len(words) == 0:
            return []
        res = []
        for x in words:
            flag = True
            if x[0] in line1:
                for i in range(1, len(x)):
                    if x[i] not in line1:
                        flag = False
                        break
            elif x[0] in line2:
                for i in range(1, len(x)):
                    if x[i] not in line2:
                        flag = False
                        break
            elif x[0] in line3:
                for i in range(1, len(x)):
                    if x[i] not in line3:
                        flag = False
                        break
            if flag:
                res.append(x)
        return res

    def findWords(self, words):
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')

        res = []
        for x in words:
            set_x = set(x.lower())
            if a & set_x == set_x or b & set_x == set_x or c & set_x == set_x:
                res.append(x)
        return res


words = ["Hello", "Alaska", "Dad", "Peace"]
print(Solution().findWords(words))
