class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtypr: Void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)
    
    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

sln = Solution()
l = [1, 2, 3]
sln.nextPermutation(l)
print(l)
l = [3, 2, 1]
sln.nextPermutation(l)
print(l)
l = [1, 1, 5]
sln.nextPermutation(l)
print(l)