"""
128. Longest Consecutive Sequence - Medium
https://neetcode.io/problems/longest-consecutive-sequence/question

Approach: - Conver array to set to manage duplicates and searching time complexity.
          - Find every number that has no back neighbour, and check how many front neighbours it has
          
TIME:0(n)
SPACE: 0(n)

Mistake: Brute forcing it.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        largest = 0
        for n in nums:
            if (n - 1) not in nums:
                i = 1
                length = 1
                while (n + i) in nums:
                    length += 1
                    i += 1
                if length > largest:
                    largest = length
                
        return largest
