class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in dict:
                if not stack or stack.pop() != dict[c]:
                    return False
            else:
                stack.append(c)
        return not stack

sln = Solution()
print(sln.isValid('()'))
print(sln.isValid('()[]{}'))
print(sln.isValid('([{}])'))
print(sln.isValid('(]'))
print(sln.isValid('([)]'))