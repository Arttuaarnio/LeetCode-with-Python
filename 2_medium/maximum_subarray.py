# Vastaus kopioitu suoraan LeetCode:n editorista

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current_sum = max_global_sum =nums[0]
        for i in range(1, len(nums)):
            max_current_sum = max(nums[i], max_current_sum + nums[i])
            if max_current_sum > max_global_sum:
                max_global_sum = max_current_sum
        return max_global_sum