# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first_step, second_step = 1, 2
        for i in range(3, n + 1):
            first_step, second_step = second_step, first_step + second_step
        return second_step
    
n = 5
solution = Solution()
print(solution.climbStairs(n))  # Output: 8