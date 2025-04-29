# Vastaus kopioitu suoraan LeetCode:n editorista

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        nums_length = len(nums)
        if nums_length % 2 == 1:
            return float(nums[nums_length // 2])
        else:
            return (nums[nums_length // 2 - 1] + nums[nums_length // 2]) / 2