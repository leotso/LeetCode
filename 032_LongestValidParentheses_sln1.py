class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxans = 0
        dp = [0 for i in xrange(len(s))]
        for i in xrange(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0) + 2
                maxans = max(maxans, dp[i])
        return maxans

sln = Solution()
print(sln.longestValidParentheses('(()'))
print(sln.longestValidParentheses(')()())'))