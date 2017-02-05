class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtypr: str
        """
        if strs == None or len(strs) == 0:
            return ""
        return self._longestCommonPrefix(strs, 0, len(strs)-1)

    def _longestCommonPrefix(self, strs, l, r):
        if l == r:
            return strs[l]
        mid = (l + r) / 2
        lcpLeft = self._longestCommonPrefix(strs, l, mid)
        lcpRight = self._longestCommonPrefix(strs, mid+1, r)
        return self.commonPrefix(lcpLeft, lcpRight)
    
    def commonPrefix(self, sLeft, sRight):
        m = min(len(sLeft), len(sRight))
        for i in xrange(m):
            if sLeft[i] != sRight[i]:
                return sLeft[0:i]
        return sLeft[0:m]


sln = Solution()
ls = ['leets', 'leetcode', 'leet', 'leeds']
print(sln.longestCommonPrefix(ls))