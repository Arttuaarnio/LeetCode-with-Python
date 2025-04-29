# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current_sum = max_global_sum =nums[0]
        for i in range(1, len(nums)):
            max_current_sum = max(nums[i], max_current_sum + nums[i])
            if max_current_sum > max_global_sum:
                max_global_sum = max_current_sum
        return max_global_sum
    
solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.maxSubArray(nums))  # Output: 6 

nums = [1]
print(solution.maxSubArray(nums))  # Output: 1 
