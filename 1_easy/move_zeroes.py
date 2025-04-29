# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1

nums = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
        