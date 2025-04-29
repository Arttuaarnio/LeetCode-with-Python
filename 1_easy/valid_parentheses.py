# Tehtävää on muokattu ja lisätty testiesimerkki LeetCodesta, jotta sen pystyy suorittamaan!

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')':'(','}':'{',']':'['}
        for char in s:
            if char in parentheses.values():
                stack.append(char)
            elif char in parentheses:
                if not stack or stack[-1] != parentheses[char]:
                    return False
                stack.pop()
            else:
                return False  
        return not stack
    
solution = Solution()
s = "()[]{}"
print(solution.isValid(s))  # Output: True

s = "(]"
print(solution.isValid(s))  # Output: False