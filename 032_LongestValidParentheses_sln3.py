class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = maxlen = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, right * 2)
            elif right > left:
                left = right = 0
        left = right = 0
        for c in reversed(s):
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, left * 2)
            elif left > right:
                left = right = 0
        return maxlen

sln = Solution()
print(sln.longestValidParentheses('(()'))
print(sln.longestValidParentheses(')()())'))
print(sln.longestValidParentheses('())(((())'))