class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = (len(nums1) + len(nums2) + 1) >> 1
        r = (len(nums1) + len(nums2) + 2) >> 1
        return (self.getkth(nums1, nums2, l) + self.getkth(nums1, nums2, r)) / 2.0
    
    def getkth(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.getkth(nums2, nums1, k)
        if m == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        
        i = min(m, k / 2)
        j = min(n, k / 2)
        if nums1[i - 1] > nums2[j - 1]:
            return self.getkth(nums1, nums2[j:], k - j)
        else:
            return self.getkth(nums1[i:], nums2, k - i)


sln = Solution()
nums1 = [1, 2, 5, 7, 8, 9]
nums2 = [3, 4]
print(sln.findMedianSortedArrays(nums1, nums2))