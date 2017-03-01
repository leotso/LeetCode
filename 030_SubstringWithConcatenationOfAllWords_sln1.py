class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtypr: List[int]
        """
        if not s or not words or not words[0]:
            return []
        lenS = len(s)
        lenWord = len(words[0])
        lenWordsChar = len(words) * lenWord
        wDic = {}
        for w in words:
            wDic[w] = wDic[w] + 1 if w in wDic else 1
        ans = []
        for i in xrange(min(lenWord, lenS - lenWordsChar + 1)):
            self._findSubString(i, i, lenS, lenWord, lenWordsChar, s, wDic, ans)
        return ans

    def _findSubString(self, left, right, lenS, lenWord, lenWordsChar, s, wDic, ans):
        curr = {}
        while right + lenWord <= lenS:
            w = s[right:right + lenWord]
            right += lenWord
            if w not in wDic:
                left = right
                curr.clear()
            else:
                curr[w] = curr[w] + 1 if w in curr else 1
                while curr[w] > wDic[w]:
                    curr[s[left:left + lenWord]] -= 1
                    left += lenWord
                if right - left == lenWordsChar:
                    ans.append(left)

sln = Solution()
s = "barfoothefoobarman"
#words = ["foo", "bar"]
words = ["foo", "bar", "foo", "bar", "the", "man"]
print(sln.findSubstring(s, words))