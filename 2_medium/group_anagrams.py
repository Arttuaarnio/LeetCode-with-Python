# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word) 
        return list(anagram_map.values())
    
solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))  
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]