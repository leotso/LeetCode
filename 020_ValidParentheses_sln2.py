class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {')':'(', '}':'{', ']':'['}
        st = []
        for e in s:
            if st and (e in map and st[-1] == map[e]):
                st.pop()
            else:
                st.append(e)
        return not st

sln = Solution()
print(sln.isValid('()'))
print(sln.isValid('()[]{}'))
print(sln.isValid('([{}])'))
print(sln.isValid('(]'))
print(sln.isValid('([)]'))