class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtypr: int
        """
        i = 0
        n = len(nums)
        while i<n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n

sln = Solution()
nums = [3,2,2,3]
val = 3
print(sln.removeElement(nums, val))