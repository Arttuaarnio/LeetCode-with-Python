# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

class Solution:
    def isPalindrome(self, x: int) -> bool:
            x = str(x)
            if x == x[::-1]:
                return True
            else:
                return False
            
x = 121
solution = Solution()
print(solution.isPalindrome(x))  # Output: True