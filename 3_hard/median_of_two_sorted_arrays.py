# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        nums_length = len(nums)
        if nums_length % 2 == 1:
            return float(nums[nums_length // 2])
        else:
            return (nums[nums_length // 2 - 1] + nums[nums_length // 2]) / 2
        
solution = Solution()

nums1 = [1, 3]
nums2 = [2]
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.5