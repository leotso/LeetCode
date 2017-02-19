class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtypr: int
        """
        i = 0
        for j in xrange(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

sln = Solution()
nums = [3,2,2,3]
val = 3
print(sln.removeElement(nums, val))