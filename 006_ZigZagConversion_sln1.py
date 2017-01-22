class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        l = []
        for i in xrange(numRows):
            l.append([])
        i = 0
        while i < n:
            for idx in xrange(numRows):
                if i >= n: break
                l[idx].append(s[i])
                i += 1
            for idx in reversed(xrange(1, numRows - 1)):
                if i >= n: break
                l[idx].append(s[i])
                i += 1
        s = ''
        for idx in xrange(numRows):
            s += ''.join(l[idx])
        return s

sln = Solution()
print(sln.convert("PAYPALISHIRING", 3))