from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        if l % 2 == 0:
            a = nums1[l // 2 - 1]
            b = nums1[l // 2]
            return (a + b) / 2
        return nums1[l // 2]

