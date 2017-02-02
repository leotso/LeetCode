class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtypr: str
        """
        if strs == None or len(strs) == 0:
            return ''
        for i in xrange(len(strs[0])):
            c = strs[0][i]
            for j in xrange(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]

sln = Solution()
ls = ['leets', 'leetcode', 'leet', 'leeds']
print(sln.longestCommonPrefix(ls))