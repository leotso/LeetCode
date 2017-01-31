class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s:str
        :rtype: int
        """
        n = len(s)
        ans = 0
        dic = {}
        i = 0
        for j in xrange(n):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            ans = max(ans, j - i + 1)
            dic[s[j]] = j + 1
            
        return ans


sln = Solution()
testString = "testString"
length = sln.lengthOfLongestSubstring(testString)
print(length)
