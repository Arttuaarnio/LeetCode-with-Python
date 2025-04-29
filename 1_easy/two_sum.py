# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
       for first_index in range(len(nums) - 1):
            for second_index in range(first_index + 1, len(nums)):
                if nums[first_index] + nums[second_index] == target:
                    return [first_index, second_index]

nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))  # Output: [0, 1]