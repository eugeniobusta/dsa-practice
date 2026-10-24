"""
1. Two Sum - Easy
https://neetcode.io/problems/two-integer-sum/question

Approach: Empty Dictionary. Store seen numbers and their position.
            if the complement needed is in the dictionary, output 
            both positions
            
TIME:0(n)
SPACE: 0(n)

Mistake: Made the bruit force solution with two for loops.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # number: index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i    
