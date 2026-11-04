"""
125. Valid Palindrome - Easy
https://neetcode.io/problems/is-palindrome/history?list=neetcode150&submissionIndex=2

Approach: TWO OPTIONS:
        1st: Using Python Built in Functions.
             - create a new string with only alpha Numeric character, then compare with its reversed
        2nd: Using Two Pointers.
             - compare left and right ONLY when alphanumeric
             - output False if ever not equal, True at the end.
             - Use ASCII characters
TIME:0(n)
SPACE: 0(1)

Mistake: Did not use two pointers
"""

# Video Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


# 1st Solution using PYTHON BUILT IN FUNCTIONS
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for ch in s:
            if ch.isalnum():
                string += ch.lower()
        return string == string[::-1]
