"""

"""

import collections


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = len([secret[i] for i in range(len(secret)) if secret[i] == guess[i]])
        cows = len(secret) - sum((collections.Counter(secret) - collections.Counter(guess)).values())
        return str(bulls) + 'A' + str(cows-bulls) + 'B'

print(Solution().getHint("1123", "0111"))
print(Solution().getHint("1807", "7810"))
print(Solution().getHint("1122", "3456"))