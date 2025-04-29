# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = Counter(nums1)
        result = []
        for number in nums2:
            if nums1_counter[number] > 0:
                result.append(number)
                nums1_counter[number] -= 1
        return result

nums1 = [1,2,2,1]
nums2 = [2,2]
solution = Solution()
print(solution.intersect(nums1, nums2)) # Output: [2, 2]