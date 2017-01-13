class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        ans = 0
        for i in range(length):
            for j in range(i+1, length+1):
                if (self.allUnique(s, i, j)):
                    ans = max(ans, j - i)
        return ans
    
    def allUnique(self, s, start, end):
        sets = set()
        for i in range(start, end):
            ch = s[i]
            if ch in sets:
                return False
            sets.add(ch)
        return True


sln = Solution()
testString = "testString"
length = sln.lengthOfLongestSubstring(testString)
print(length)