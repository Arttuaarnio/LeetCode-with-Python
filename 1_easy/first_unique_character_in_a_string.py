# Vastaus kopioitu suoraan LeetCode:n editorista

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for index, character in enumerate(s):
            if count[character] == 1:
                return index
        return -1