class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        remains = abs(x)
        sign = -1 if x < 0 else 1

        result = 0
        while remains != 0:
            tail = remains % 10
            newResult = result * 10 + tail
            if (newResult - tail) / 10 != result:
                return 0
            result = newResult
            remains = remains / 10
        
        return result * sign

sln = Solution()
print(sln.reverse(123))
print(sln.reverse(-123))
print(sln.reverse(12300))