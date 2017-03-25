class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return n
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

sln = Solution()
nums = [1,3,5,6]
print(sln.searchInsert(nums, 5))
print(sln.searchInsert(nums, 2))
print(sln.searchInsert(nums, 7))
print(sln.searchInsert(nums, 0))