class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s:str
        :rtype: int
        """
        n = len(s)
        ans = i = j = 0
        sets = set()
        while i < n and j < n:
            if s[j] in sets:
                sets.remove(s[i])
                i+=1
            else:
                sets.add(s[j])
                j+=1
                ans = max(ans, j - i)
        return ans


sln = Solution()
testString = "testString"
length = sln.lengthOfLongestSubstring(testString)
print(length)