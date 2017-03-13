class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxans = 0
        stack = []
        stack.append(-1)
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans

sln = Solution()
print(sln.longestValidParentheses('(()'))
print(sln.longestValidParentheses(')()())'))
print(sln.longestValidParentheses('())(((())'))