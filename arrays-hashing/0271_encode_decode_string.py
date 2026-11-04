"""
271. Encode Decode String - Medium
https://neetcode.io/problems/string-encode-and-decode/question

Approach: ENCODE:
          - grab each word, and add its length and a separator "#"
          DECODE:
          - first ch will ALWAYS be number. augment position finding i
          by 1, the length of the word, and the position j we were in
          - append ONLY the word. From AFTER j which is "#" + length of the word
            
TIME:0(n)
SPACE: 0(n)

Mistake: Always though the number would be a single digit. Didnt account for double digits.
         Assumed length <= 9
"""

# Solution done after looking at the NEETCODE Video.
class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word)) + "#" + word
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return output

# 1st Solution, no hints. 34/60 cases
class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += str(len(word)) + "#" + word
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        for i in range(1, len(s)):
            if s[i - 1].isdigit() and s[i] == "#":
                output.append(s[i + 1:i + 1 + int(s[i - 1])])
        return output
