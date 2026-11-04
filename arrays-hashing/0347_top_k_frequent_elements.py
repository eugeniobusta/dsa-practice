"""
347. Top K Frequent Elements - Medium
https://neetcode.io/problems/top-k-elements-in-list/question

Approach: BucketSort, create a frequencies list where each index is the number of appearences.
          Frequences length will == len(nums) + 1 (since indexing starts at 0)
          each num will be appended in Freq position of appearence
          Then search backwards through Freq till we gather K elements (from most appearences to least)
            
TIME:0(n)
SPACE: 0(n)

Mistake: First solution O(m log n), since sorting, creating and finding.
"""

# Solution using Bucket Sort, after hints
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        output = []
        for pos in range(len(freq) - 1, 0, -1):
            for e in freq[pos]:
                output.append(e)
            if len(output) == k:
                return output


# 1st Solution. No hints, first impression.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        found = {}
        for num in nums:
            found[num] = found.get(num, 0) + 1

        output = []
        found = dict(sorted(found.items(), key=lambda x: x[1], reverse=True))
        seen = 0
        for num in found:
            output.append(num)
            seen += 1
            if seen == k:
                return output
