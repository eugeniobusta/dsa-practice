"""
242. Valid Anagram - Easy
https://leetcode.com/problems/valid-anagram/description/

Approach: Dictionary to count every character, then remove with second string everytime
            we see a character. Output False at any point where it makes it already impossible
TIME:0(n)
SPACE: 0(n)

Mistake: Made a 0(n^2) Time Complexity, using replace() on strings. 
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1
            """
            Same thing as the top line
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
            """

        for ch in t:
            if ch not in count:
                return False

            count[ch] -= 1

            if count[ch] < 0:
                return False

        return True
