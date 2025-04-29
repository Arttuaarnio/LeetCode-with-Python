# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for character, count in ransom_note_count.items():
            if magazine_count[character] < count:
                return False
        return True

ransomNote = "aa"
magazine = "aab"
solution = Solution()
print(solution.canConstruct(ransomNote, magazine))  # Output: True