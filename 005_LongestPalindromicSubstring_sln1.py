class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        for i in xrange(n):
            subLen = n - i
            for j in xrange(n - subLen + 1):
                subStr = s[j:j + subLen - 1]
                if self.isPalindrome(subStr):
                    return subStr

    def isPalindrome(self, s):
        n = len(s)
        if n == 1:
            return True
        for i in xrange(n / 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True


sln = Solution()
s = "babad"
palindromeStr = sln.longestPalindrome(s)
print(palindromeStr)