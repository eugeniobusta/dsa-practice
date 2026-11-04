"""
167. Two Integer Sum II - Medium
https://neetcode.io/problems/two-integer-sum-ii/question

Approach: - pointer i (left) moves right ONLY if the sum is too small
          - pointer j (right) moves left ONLY if the sum is too big
          - Return if ever equal
TIME:0(n)
SPACE: 0(1)

Mistake: Brute forced it, by checking for each element every possible sum that could equal the target.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < len(numbers):
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]

        return []
