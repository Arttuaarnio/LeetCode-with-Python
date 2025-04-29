# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)
    
accounts = [[1, 2, 3], [3, 2, 1]]
solution = Solution()
print(solution.maximumWealth(accounts))  # Output: 6