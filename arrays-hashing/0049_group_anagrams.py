"""
1. Group Anagrams - Medium
https://neetcode.io/problems/anagram-groups/question

Approach: Empty Dictionary. Keys are lists with 26 0s, one for each letter, then count for each.
          if a word has the same letters, add to the value of the key.
          Return each value
            
TIME: O(m * n * 26) = O(m * n)

Mistake: Didn't make use of ascii .
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())
