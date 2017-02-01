class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtypr: str
        """
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for s in strs:
            while s.find(prefix) != 0:
                prefix = prefix[0: len(prefix)-1]
                if (prefix == ''):
                    return ''
        return prefix

sln = Solution()
ls = ['leets', 'leetcode', 'leet', 'leeds']
print(sln.longestCommonPrefix(ls))