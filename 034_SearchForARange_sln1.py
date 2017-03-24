class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        result = [-1, -1]
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if nums[lo] != target:
            return result
        else:
            result[0] = lo
        
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2 + 1
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        result[1] = hi
        return result

sln = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(sln.searchRange(nums,target))