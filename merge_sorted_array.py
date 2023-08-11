class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        
        for i in range(len(nums1) - 1, -1, -1):
            if m < 0:
                nums1[i] = nums2[n]
                n -= 1
            elif n < 0 or nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
