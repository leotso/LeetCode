class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic and dic[complement] != 1:
                return [i, dic[complement]]
        return None

sln = Solution()
nums = [2, 7, 11, 15]
target = 9
print(sln.twoSum(nums, target))