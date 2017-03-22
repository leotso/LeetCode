class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) / 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target == nums[lo] else -1

sln = Solution()
print(sln.search([4, 5, 6, 7, 0, 1, 2], 3))
print(sln.search([4, 5, 6, 7, 0, 1, 2], 5))
print(sln.search([4, 5, 6, 7, 0, 1, 2], 2))