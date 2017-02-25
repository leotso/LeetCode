class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ls = len(haystack)
        lt = len(needle)
        if ls < lt: return -1
        for i in xrange(ls-lt+1):
            if haystack[i:i+lt]==needle:
                return i
        return -1

sln = Solution()
print(sln.strStr('haystack', 'stack'))