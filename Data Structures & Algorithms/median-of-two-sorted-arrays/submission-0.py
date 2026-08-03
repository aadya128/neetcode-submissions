class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        add = sorted(nums1 + nums2)
        n = len(add)

        if n % 2:
            return float(add[n // 2])

        return (add[n // 2 - 1] + add[n // 2]) / 2.0