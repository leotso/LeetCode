class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        ls = list(s.strip())
        if len(ls) == 0 : return 0
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))

sln = Solution()
print(sln.myAtoi(' '))
print(sln.myAtoi(' 12'))
print(sln.myAtoi(' -12'))
print(sln.myAtoi('- 12'))
print(sln.myAtoi(' -12k '))