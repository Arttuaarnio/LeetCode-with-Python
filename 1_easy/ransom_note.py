# Vastaus kopioitu suoraan LeetCode:n editorista

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for character, count in ransom_note_count.items():
            if magazine_count[character] < count:
                return False
        return True