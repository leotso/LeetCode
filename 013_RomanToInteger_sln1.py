class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in reversed(s):
            if c == 'I':
                res += (-1 if res >= 5 else 1)
                continue
            if c == 'V':
                res += 5
                continue
            if c == 'X':
                res += 10 * (-1 if res >= 50 else 1)
                continue
            if c == 'L':
                res += 50
                continue
            if c == 'C':
                res += 100 * (-1 if res >= 500 else 1)
                continue
            if c == 'D':
                res += 500
                continue
            if c == 'M':
                res += 1000
                continue
        return res

sln = Solution()
print(sln.romanToInt('III'))
print(sln.romanToInt('XXXII'))
print(sln.romanToInt('CIII'))