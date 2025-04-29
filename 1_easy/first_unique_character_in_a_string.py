# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for index, character in enumerate(s):
            if count[character] == 1:
                return index
        return -1

s = "leetcode"
solution = Solution()
print(solution.firstUniqChar(s)) # Output: 0