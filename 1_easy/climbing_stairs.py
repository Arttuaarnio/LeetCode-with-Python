# Vastaus kopioitu suoraan LeetCode:n editorista

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first_step, second_step = 1, 2
        for i in range(3, n + 1):
            first_step, second_step = second_step, first_step + second_step
        return second_step