"""
217. Contains Duplicate - Easy
https://leetcode.com/problems/contains-duplicate/description/

Approach: Create an empty set. Introduce unseen elements into the set.
            if a number is already in the set, print TRUE. If none already 
            in the set, print FALSE
TIME:0(n)
SPACE: 0(n)

Mistake: None
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
