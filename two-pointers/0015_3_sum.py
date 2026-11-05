"""
15. 3 Sum - Medium
https://neetcode.io/problems/three-integer-sum/question

Approach: - Sort the List in ascending order. O(nlogn)
          - First pointer i to the first element, and have two other pointers, left and right
          that try to equal the i element. 
          
TIME:0(n^2)
SPACE: 0(1)

Mistake: Did not move left pointer when we check the same number
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorting
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    tmp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = tmp

        output = []
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        
        return output
