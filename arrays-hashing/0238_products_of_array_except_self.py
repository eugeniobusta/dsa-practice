"""
238. Products of Array Except Self - Medium
https://neetcode.io/problems/products-of-array-discluding-self/question

Approach: Calculate always on the output array [1] * len(nums)
          Add to each position, the prefix total which is multiplied by the next num
          --
          For postfix, Multiply each position, till -1 for out of index error.
          postfix will become the nums in nums going through the array reversively

TIME:0(n)
SPACE: 0(n)

Mistake: Made a 0(n^2) Time Complexity. 
"""

# Solution after watching NEETCODE video.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output


# 1st solution. Time complexity O(n^2)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = [1 for n in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    total[i] *= nums[j]
        return total
