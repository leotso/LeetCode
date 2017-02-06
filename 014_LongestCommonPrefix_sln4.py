class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtypr: str
        """
        if strs == None or len(strs) == 0:
            return ''
        minLen = len(strs[0])
        for s in strs:
            minLen = min(minLen, len(s))
        low, high = 1, minLen
        while low <= high:
            middle = (low + high) / 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][0:(low + high) / 2]
    
    def isCommonPrefix(self, strs, length):
        str1 = strs[0][0:length]
        for i in xrange(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True


sln = Solution()
ls = ['leets', 'leetcode', 'leet', 'leeds']
print(sln.longestCommonPrefix(ls))